#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

import time
class BankAccount(object):
    def __init__(self, label, balance, transactions=[]):
        self.label = label
        self.balance = balance
        self.transactions = transactions

    def __str__(self):
        return 'Your bank account label is {l} and your balance is {b}'.format(l=self.label, b=self.balance)

    def withdraw(self, amount):
        if amount>self.balance or amount<0:
            print('You have entered a value greater than your balance or a negative value')
        else:
            self.balance-=amount
            print('Your balance is now ${b}'.format(b = self.balance))
        #newTransact = Transaction(type='withdraw', amount=amount)
        #self.transactions.append(newTransact)

    def deposit(self, amount):
        if amount<0:
            print('You have entered a negative value')
        else:
            self.balance+=amount
            print('Your balance is now ${b}'.format(b = self.balance))
        # newTransact = Transaction(type='deposit', amount=amount)
        # self.transactions.append(newTransact)

    def rename(self, name):
        if name=="":
            print('You have entered a blank name')
        else:
            self.label = name
            print('Your bank label is now '+name)

    def transfer(self, dest_account, amount):
        if amount>self.balance:
            print("You don't have enough money to transfer that amount")
        elif amount<0:
            print("That is a negative number")
        else:
            self.balance-=amount
            dest_account.balance+=amount
        # newTransact = Transaction(type='transfer', amount=amount, dest_account=dest_account)
        # self.transactions.append(newTransact)

    def seeTransacts(self):
        print(self.transactions)

class Transaction(object):
    def __init__(type, amount, dest_account='', time=time.time):
        self.time = time
        self.type = type
        self.amount = amount
        self.dest_account = dest_account
    def __str__(self, type):
        if type=="transfer":
            return '{t}: transfer {a} to account {d}'.format(t=self.time, a=self.amount, d=self.dest_account)
        else:
            return '{t}: withdraw {a}'.format(t=self.time, a=self.amount)
