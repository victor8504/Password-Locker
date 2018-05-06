#!/usr/bin/env python3.6
from tester import User #Importing the user class
from credentials import Credential #Importing the credential class
import random

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

def main():
    print("Hey!! Welcome to your password manager. What would you like to do?")
    print('\n')

    while True:
        print("Use the following short codes : CA ~ Create a new account, DA ~ Display your accounts, FA ~ Find an account, EX ~ Exit the account list")

        short_code = input().upper()

        if short_code == 'CA':

            print("New Account")
            print("*"*20)

            print("Account name ...")
            acc_name = input()

            print("Email Address ...")
            email = input()

            print("Password")
            password = input()

            save_accounts(create_account(acc_name,email,password)) # create and save new account.
            print ('\n')
            print(f"New Account {acc_name} {email} created")
            print ('\n')

        elif short_code == 'DA':

            if display_accounts():
                print("Here is a list of all your accounts")
                print('\n')

                for account in display_accounts():
                    print(f"{account.account_name} {account.email_address} -----{account.password}")

                print('\n')
            else:
                print('\n')
                print("You don't seem to have any accounts saved yet")
                print('\n')

        elif short_code == 'FA':

            print("Enter the account name you want to search for")

            search_account = input()
            if check_existing_accounts(search_account):
                search_account = find_account(search_account)
                print(f"{search_account.account_name} {search_account.email_address}")
                print('*'*20)

                print(f"Account Name ------{search_account.account_name}")
                print(f"Email address ------{search_account.email_address}")
            else:
                print("That account does not exist")

        elif short_code == "EX":
            print("Thank you for visiting Password Locker. Make sure to visit again!")


if __name__ == '__main__':

    main()