#!/usr/bin/python3
# Author: James Campbell
# Date: November 22 2015
# What: Accesses the blockchain module and queries some data as example
import sys
from sys import exit
import datetime
from blockchain import blockexplorer
if sys.version_info < (3, 0):
    # Python 2
    from Tkinter import *
else:
    # Python 3
    from tkinter import *

def show_entry_fields():
   print("Address: %s\n\n" % (e1.get()))
   get_bitcoin_wallet()

def get_bitcoin_wallet():
    address = blockexplorer.get_address(e1.get())
    var.set(address.final_balance)
    resultlabel.set("Current Balance:")
    hashlabel.set("Transaction History:")
    stringer = ''
    transactions = address.transactions
    for trans in transactions:
        timestamp = trans.time
        fixedtime = datetime.datetime.fromtimestamp(timestamp)
        fixer = fixedtime.strftime('%Y-%m-%d %H:%M:%S')
        stringer = stringer + "hash: " + trans.hash + "\ntime: " + fixer + "\nip relay: " + str(trans.relayed_by) + "\n"
    hashlist.set(stringer)
master = Tk()
resultlabel = StringVar()
var = StringVar()
hashlist = StringVar()
hashlabel = StringVar()
Label(master, text="Bitcoin address:",justify=RIGHT).grid(row=0)

e1 = Entry(master, justify=LEFT)
Label(master,textvariable = resultlabel,justify=RIGHT).grid(row=1)
Label(master,textvariable = hashlabel).grid(row=2)
Label(master, textvariable = var,justify=LEFT).grid(sticky = W, row=1, column=1)
Label(master,textvariable = hashlist,justify=LEFT).grid(row=2, column=1)
e1.grid(sticky = W, row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
