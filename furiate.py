#!/usr/bin/env python

import getpass
import time

from web3 import Web3, HTTPProvider
from eth_account import Account # will use directly instead of through web3 provider

from schedule import chainids, txs

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

# get nonces on all chains
nonces = {}
for net, w3 in w3s.items():
    print(net, 'block', w3.eth.getBlock('latest')['number'])
    nonces[net] = w3.eth.getTransactionCount(acct.address)
print('Nonces:', nonces)

print(time.ctime())

for nonce, tx in txs.items():
    # populate "missing" key
    tx['nonce'] = nonce

    for net, w3 in w3s.items():
        # skip txs already in the chain
        if tx['nonce'] <= nonces[net]:
            print('Transaction with nonce', tx['nonce'], 'already exists on', net, '- skipping...')
            continue

        # infura doesn't like chainId==0, so be explicit
        tx['chainId'] = chainids[net]

        # TODO: other ways to specify?..
        if 'gasPrice' not in tx.keys():
            tx['gasPrice'] = w3.eth.gasPrice

            signed = acct.signTransaction(tx)

            txhash = w3.eth.sendRawTransaction(signed.rawTransaction)
            print(net, 'tx with nonce', tx['nonce'], 'txhash', Web3.toHex(txhash))
