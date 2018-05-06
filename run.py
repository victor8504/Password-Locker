#!/usr/bin/env python3.6
from tester import User #Importing the user class

def create_account(accname,email,password):

    '''
    Function to create a new account
    '''

    new_account = User(accname,email,password)
    return new_account

def save_accounts(account):

    '''
    Function to save account
    '''

    account.save_account()