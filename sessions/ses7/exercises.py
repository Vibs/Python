#
#

#¤ Exercise 2: Bank
# In the exercise from last monday with the bank, account and customer, change the code to use properties instead of the public variables.

class Bank:
     def __init__(self):
        self.__accounts = []

class Account:
     def __init__(self, no, cust):
        self.no = no
        self.cust = cust

class Customer:
     def __init__(self, name):
        self.name = name

#& The bank class should futher be change into not taking any accounts as parameters at initialization.

class Bank:
    def __init__(self):
        self.accounts = []
    
    @property
    def accounts(self, acc):
        return self.__accounts
    @accounts.setter
    def accounts(self, acc):
        if type(acc) is int: # hvis den er en integer
            self.__accounts.append(acc) # det er HER jeg gør den private via __
        elif type(acc) in [tuple, list]: # hvis den er enten tuple eller list (altså er en collection)
            for i in acc:
                self.__accounts.append(i)

#& The accouts should be added afterwards, eithers as a single account one at a time, or as a collection of accounts (many at the sametime).

#& Somewhere you should change the code so that a customer only can create one account.

#& The Customer class should make sure that the customer is over 18 year of age.