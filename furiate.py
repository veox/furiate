#!/usr/bin/env python

import getpass

from web3 import Web3, HTTPProvider

with open('infura.key') as keyfile:
    infurakey = keyfile.read()

chainids = {
    #'mainnet': 1,
    'ropsten': 3,
    'rinkeby': 4,
    'kovan': 42
}
w3s = {net: Web3(HTTPProvider('https://' + net + '.infura.io/' + infurakey)) for net in chainids.keys()}

# https://web3py.readthedocs.io/en/latest/middleware.html#geth-style-proof-of-authority
if 'rinkeby' in w3s.keys():
    from web3.middleware import geth_poa_middleware
    w3s['rinkeby'].middleware_stack.inject(geth_poa_middleware, layer=0)

acct = None
for net, w3 in w3s.items():
    # enable local key management (disabled by default in v4 beta 12)
    #w3.eth.enable_unaudited_features()

    # only ask for password once
    if acct is None:
        with open('ethereum.key') as keyfile:
            privkey = w3.eth.account.decrypt(keyfile.read(), getpass.getpass())
            acct = w3.eth.account.privateKeyToAccount(privkey)

    print(net, 'block', w3.eth.getBlock('latest')['number'])

    tx = {
        # specify explicitly to prevent accidental repeats
        'nonce': 0,
        # TODO: actual data
        'to': acct.address,
        # TODO: use estimateGas
        'gas': 90000,
        # TODO: don't rely on infura
        'gasPrice': w3.eth.gasPrice,
        # infura doesn't like chainId==0, so be explicit
        'chainId': chainids[net]
    }

    signed = w3.eth.account.signTransaction(tx, acct.privateKey)

    txhash = None
    try:
        txhash = w3.eth.sendRawTransaction(signed.rawTransaction)
    except ValueError as e:
        if e.args[0]['message'] != 'nonce too low':
            raise e
        else:
            print(net, 'Transaction with nonce', tx['nonce'], 'already exists!..')
    finally:
        print(net, 'txhash', Web3.toHex(txhash))
