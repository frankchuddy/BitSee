# BitSee
### _Version 0.1.1_
A simple OSX app to check the bitcoin balance and history for any Bitcoin Wallet address.
The history includes each transaction hash, the relay ip address of the transaction, the date time of each, as well as the current bitcoin wallet balance.

#### Language

Written in Python 3.

#### Requirements

`blockchain`, which can be installed like `pip3 install blockchain`.
`py2app`, which can be installed and working on El Capitan even via `pip install -U git+https://github.com/metachris/py2app.git@master`.

Either build your own by cloning to a folder and running:
```
$ cd BitSee
$ python3 setup.py py2app
$ cd dist
$ open BitSee.app
```

Or, just download the [latest version](https://github.com/jamesacampbell/BitSee/latest.zip).

Example of how it works. You simply paste in the wallet and it shows all transactions, hash, ip address, and date of transaction as well as the current balance of the wallet.

![bitsee](https://cloud.githubusercontent.com/assets/616585/11581300/7146f054-9a0e-11e5-81b2-f791aa8ee37d.gif)

Enjoy and please let me know how you like it. Feel free to redistribute but keep this ReadMe intact.
Made in DC by [James Campbell](https://www.jamescampbell.us).
