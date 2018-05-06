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

def del_account(account):

    '''
    Function to delete a account
    '''

    account.delete_account()

def find_account(account_name):

    '''
    Function that finds an account by account name and returns the account.
    '''

    return User.find_by_account_name(account_name)

def check_existing_accounts(account_name):

    '''
    Function that check if an account exists with that account_name and returns a Boolean.
    '''

    return User.account_exists(account_name)

def display_accounts():

    '''
    Function that returns all the saved accounts.
    '''

    return User.display_accounts()