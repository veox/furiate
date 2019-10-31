from web3 import Web3

chainids = {
    #'mainnet': 1,
    'ropsten': 3,
    'rinkeby': 4,
    'goerli': 5,
    'kovan': 42,
}

txs = {
    0: {
        'to': '', # none! (CREATE)
        'data': '0x600280600c6000396000f30030ff', # deploy: collapser
        'gas': 90000,
        # gasPrice was not set!
    },

    1: {
        'to': '0x8905C87B11507A243bbf57a17718d55F4C8A497C', # collapser
        'value': 42, # die antwoord
        'gas': 90000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    2: {
        'to': '', # none! (CREATE)
        'data': '0x60ef8061000d6000396000f3003415600a5760006000fd5b366024141560315760e060020a60003504638124b78e14602a5760006000fd5b6004356020525b3660141415604657606060020a600035046020525b60ff60205111151560575760006000fd5b6020513b60405260405160001415606e5760006000fd5b6008600e026101000360020a6d600e380380600e6000396000f3000260605260405160006060600e016020513c604051600e0160606000f06000526000516000141560b95760006000fd5b600051604052602051337f9ce1bdd7d0964c6547e8b9b894d2524b432b8483c5b8b73ea949293d876a0f8c60206040a360206000f3', # deploy: cloning-vat
        'gas': 150000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    3: {
        'to': '', # none! (CREATE)
        'data': '0x600280600c6000396000f30030ff', # deploy: collapser
        'gas': 150000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    4: {
        'to': '0xC533fFbdcc952069f710dc3f6FA08510125Bcd49', # cloning-vat
        'data': str.lower('0xAfBbec1931321D822cC024dBa9c3a783F2019C62'), # address: collapser (raw!)
        'gas': 90000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    5: {
        'to': '', # none! (CREATE)
        'data': '0x609180600c6000396000f3003415600957600080fd5b361515601457600080fd5b7f600e380380600e6000396000f300600080fd00000000000000000000000000006101205236600061013237601236016101206000f061010052610100511515605c57600080fd5b61010051604052337f88bc4af924ebbcf92aeb0f1003d65460177fa2c66e3f6800d9b00cf9b8e5f0db60206040a26020610100f3', # deploy: cannery (optimised)
        'gas': 90000, # OOPS! OoG
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    6: {
        'to': '', # none! (CREATE)
        'data': '0x609180600c6000396000f3003415600957600080fd5b361515601457600080fd5b7f600e380380600e6000396000f300600080fd00000000000000000000000000006101205236600061013237601236016101206000f061010052610100511515605c57600080fd5b61010051604052337f88bc4af924ebbcf92aeb0f1003d65460177fa2c66e3f6800d9b00cf9b8e5f0db60206040a26020610100f3', # deploy: cannery (optimised)
        'gas': 150000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    7: {
        'to': '', # none! (CREATE)
        'data': '0x61015f8061000e6000396000f300341561000a57600080fd5b7c01000000000000000000000000000000000000000000000000000000006000350460205236602414156100525760205163b95460f81461004a57600080fd5b600435610120525b60643610610074576020516361ba64051461006c57600080fd5b600435610120525b6044356101605260ff610120511161008b57600080fd5b610120513b610140526101405115156100a357600080fd5b610140516000610180610120513c7c0100000000000000000000000000000000000000000000000000000000610180510463600080fd146100e357600080fd5b6020516361ba64051415610101576101605160646101405161018001375b6004610160516101405101036101846000f06101005261010051151561012657600080fd5b6101005160405261012051337f6a5e677bbcf69000145b06b544171fc934a174f2f6761de26f6884606a6f050760206040a36020610100f3', # deploy: can-opener (optimised)
        'gas': 140000, # OOPS! OoG
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    8: {
        'to': '', # none! (CREATE)
        'data': '0x61015f8061000e6000396000f300341561000a57600080fd5b7c01000000000000000000000000000000000000000000000000000000006000350460205236602414156100525760205163b95460f81461004a57600080fd5b600435610120525b60643610610074576020516361ba64051461006c57600080fd5b600435610120525b6044356101605260ff610120511161008b57600080fd5b610120513b610140526101405115156100a357600080fd5b610140516000610180610120513c7c0100000000000000000000000000000000000000000000000000000000610180510463600080fd146100e357600080fd5b6020516361ba64051415610101576101605160646101405161018001375b6004610160516101405101036101846000f06101005261010051151561012657600080fd5b6101005160405261012051337f6a5e677bbcf69000145b06b544171fc934a174f2f6761de26f6884606a6f050760206040a36020610100f3', # deploy: can-opener (optimised)
        'gas': 250000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    9: {
        'to': '0x25d62DA8E032c5cba01c351c7868f4b1a0E0949e', # cannery
        'data': '0x600280600c6000396000f30030ff', # bytecode for: deploy: collapser
        'gas': 150000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    10: {
        'to': '0xC9d28DcA3CD8cCFDF583643837E3C637Bc59A789', # can-opener
        'data': str.lower('1e77625c9818c25d4f4FA6b40D24Ef231D1740eF'), # OOPS! incorrect calldatalen
        'gas': 150000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    11: {
        'to': '0xC9d28DcA3CD8cCFDF583643837E3C637Bc59A789', # can-opener
        'data': '0xb95460f8' + '0'*24 + str.lower('1e77625c9818c25d4f4FA6b40D24Ef231D1740eF'), # open(address(canned-collapser))
        'gas': 150000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    12: {
        'to': '', # none! (CREATE)
        'data': '0x608080600c6000396000f3003415600957600080fd5b60e060020a6000350460205263c85e07b96020511415606a576000805259600052601480606c600051396000516000f0606052606051604052337f9f0f13e03835c7dcca2675cb51976e07bd186b2e351cefe0db24ec0fe62105ef60206040a25b00602a6113375560028060126000396000f30030ff', # deploy: collapser-stamping-press (optimised) (old)
        'gas': 150000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    13: {
        'to': '0xE725E70c7A00fF3Fb32B6C01Cce44600710d673e', # collapser-stamping-press (old)
        'data': '0xc85e07b9', # stamp()
        'gas': 90000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    # the following three have been batched in a single run
    14: {
        'to': '0xE16f7d74353e2822E85d68b8a8DE2ae02f80486E', # uncanned-collapser (from nonce 11)
        'gas': 25000, # OOPS! OoG
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },
    15: {
        'to': '0xB7521f1Ba8c23dc60962D8cF8F842AAD46B3873A', # cloned-collapser (from nonce 4)
        'gas': 25000, # OOPS! OoG
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },
    16: {
        'to': '0x8cAF1dc82a0Fabc1374E5246C506dEAeD974789b', # stamped-collapser (from nonce 13)
        'gas': 25000, # OOPS! OoG
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    # the following three have been batched in a single run
    17: {
        'to': '0xE16f7d74353e2822E85d68b8a8DE2ae02f80486E', # uncanned-collapser (from nonce 11)
        'gas': 42000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },
    18: {
        'to': '0xB7521f1Ba8c23dc60962D8cF8F842AAD46B3873A', # cloned-collapser (from nonce 4)
        'gas': 42000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },
    19: {
        'to': '0x8cAF1dc82a0Fabc1374E5246C506dEAeD974789b', # stamped-collapser (from nonce 13)
        'gas': 42000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    20: {
        'to': '', # none! (CREATE)
        'data': '0x60898061000d6000396000f3003415600957600080fd5b60e060020a6000350460205263c85e07b96020511415606f5760008052596000526014806075600051396000516000f0606052606051604052337f9f0f13e03835c7dcca2675cb51976e07bd186b2e351cefe0db24ec0fe62105ef60206040a260206060f35b600080fd00602a6113375560028060126000396000f30030ff', # deploy: updated stamping-press: collapser (optimised)
        'gas': 150000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    21: {
        'to': '0xb20ad6089B9BEDCF6dDaadc4D9A56AD86694359a', # updated stamping-press
        'data': '0xc85e07b9', # stamp()
        'gas': 90000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },

    22: {
        'to': '0x7CEFB94598C954b3Cabf6a8d57dBaE822321Ff53', # stamped-collapser (from nonce 21)
        'gas': 42000,
        'gasPrice': Web3.toWei(1337, 'lovelace'),
    },
}
