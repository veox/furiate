# furiate

Simple `web3.py` script to execute the same transaction on main-net
and three major test-nets.

Most useful for deploying contracts with the same address on all chains.

Inspired by [the "Astral Projection" article][ap] by Richard Moore.

[ap]: https://blog.ricmoo.com/contract-addresses-549074919ec8

## Installation

In a Python 3 `virtualenv`:

``` python
pip install -r requirements.txt
```

`ethereum.key` should be a "JSON keyfile".

`infura.key` should contain one line with the Infura access token.

## Using

Send ether to the account on all specified chains.

Modify `schedule.py` to your liking.

Run the `furiate.py` script.
