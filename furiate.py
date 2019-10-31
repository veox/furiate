#!/usr/bin/env python

import getpass
import time

from web3 import Web3, HTTPProvider
from eth_account import Account # will use directly instead of through web3 provider

from schedule import chainids, txs

print(len(txs), 'transactions in schedule.')

with open('infura.key') as keyfile:
    infurakey = keyfile.read()

w3s = {
    net: Web3(HTTPProvider('https://' + net + '.infura.io/v3/' + infurakey))
    for net in chainids.keys()
}

# https://web3py.readthedocs.io/en/latest/middleware.html#geth-style-proof-of-authority
if 'rinkeby' in w3s.keys():
    from web3.middleware import geth_poa_middleware
    w3s['rinkeby'].middleware_stack.inject(geth_poa_middleware, layer=0)

# only ask for password once
with open('ethereum.key') as keyfile:
    privkey = Account.decrypt(keyfile.read(), getpass.getpass())
    acct = Account.privateKeyToAccount(privkey)

# get nonces on all chains
chainnonces = {}
for net, w3 in w3s.items():
    print(net, 'block', w3.eth.getBlock('latest')['number'])
    chainnonces[net] = w3.eth.getTransactionCount(acct.address) - 1
print('Nonces present:', chainnonces)

print('Starting run:', time.ctime())

for nonce, tx in txs.items():
    # don't even consider nonces present on all chains
    if nonce < min(chainnonces.values()):
        continue
    if nonce == min(chainnonces.values()):
        print('Nonces up to (and including)', nonce, 'present on all chains - skipping...')
        continue

    # populate "missing" key
    tx['nonce'] = nonce

    for net, w3 in w3s.items():
        # skip txs already in _this_ chain
        if tx['nonce'] <= chainnonces[net]:
            print('Transaction with nonce', tx['nonce'], 'already included on', net, '- skipping...')
            continue

        # infura doesn't like chainId==0, so be explicit
        tx['chainId'] = chainids[net]

        # TODO: other ways to specify?..
        if 'gasPrice' not in tx.keys():
            tx['gasPrice'] = w3.eth.gasPrice

        signed = acct.signTransaction(tx)

        try:
            txhash = w3.eth.sendRawTransaction(signed.rawTransaction)
            print(net, 'tx with nonce', tx['nonce'], 'txhash', Web3.toHex(txhash))
        except ValueError as e:
            errorcode = e.args[0]['code']

            # 'invalid sender' (everywhere?..) and 'transaction already imported' (kovan)
            if errorcode != -32000 and errorcode != -32010:
                raise e
            else:
                print('Transaction with nonce', tx['nonce'], 'already submitted to', net)
