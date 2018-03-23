# furiate

Simple `web3.py` script to execute the same transaction on main-net
and three major test-nets.

Most useful for deploying contracts with the same address on all chains.

## Installation

In a Python 3 `virtualenv`:

``` python
pip install -r requirements.txt
```

`ethereum.key` should be a "JSON keyfile".

`infura.key` should contain one line with the Infura access token.

## Using

Search for `MODIFY` in the script body and edit the sections to your
liking.

Send ether to the account on all specified chains.

When done, run the script.
