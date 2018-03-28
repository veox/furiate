#!/usr/bin/env python

import getpass
import time

from web3 import Web3, HTTPProvider
from eth_account import Account # will use directly instead of through web3 provider

# MODIFY
chainids = {
    'mainnet': 1,
    'ropsten': 3,
    'rinkeby': 4,
    'kovan': 42
}

# MODIFY
import schedule
tx = schedule.tx

# flop if gas too low
if tx['to'] == '' and tx['data'] != '' and tx['gas'] <= 100000:
    raise Exception('Gas quite likely too low for deployment!')

with open('infura.key') as keyfile:
    infurakey = keyfile.read()

w3s = {net: Web3(HTTPProvider('https://' + net + '.infura.io/' + infurakey)) for net in chainids.keys()}

# https://web3py.readthedocs.io/en/latest/middleware.html#geth-style-proof-of-authority
if 'rinkeby' in w3s.keys():
    from web3.middleware import geth_poa_middleware
    w3s['rinkeby'].middleware_stack.inject(geth_poa_middleware, layer=0)

# only ask for password once
with open('ethereum.key') as keyfile:
    privkey = Account.decrypt(keyfile.read(), getpass.getpass())
    acct = Account.privateKeyToAccount(privkey)

print(time.ctime())

nonces = {}
for net, w3 in w3s.items():
    print(net, 'block', w3.eth.getBlock('latest')['number'])
    nonces[net] = w3.eth.getTransactionCount(acct.address)
if len(set(list(nonces.values()))) > 1:
    print('OOPS! nonces:', nonces)
    raise Exception('Nonces do not line up!')

for net, w3 in w3s.items():
    # infura doesn't like chainId==0, so be explicit
    tx['chainId'] = chainids[net]

    # TODO: other ways to specify?..
    if 'gasPrice' not in tx.keys():
        tx['gasPrice'] = w3.eth.gasPrice

    signed = acct.signTransaction(tx)

    txhash = None
    try:
        txhash = w3.eth.sendRawTransaction(signed.rawTransaction)
        print(net, 'txhash', Web3.toHex(txhash))
    except ValueError as e:
        errorcode = e.args[0]['code']

        # 'invalid sender' (everywhere?..) and 'transaction already imported' (kovan)
        if errorcode != -32000 and errorcode != -32010:
            raise e
        else:
            print(net, 'transaction with nonce', tx['nonce'], 'already exists!..')
