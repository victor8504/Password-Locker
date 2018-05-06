class User:

    '''
    Class that generates new instances of users
    '''

    user_list = [] # Empty user list

    def __init__(self, account_name, email_address, password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
        account_name: New user account name.
        email_address: New user email address.
        password: New user password.
        '''

        self.account_name = account_name
        self.email_address = email_address
        self.password = password

    def save_account(self):

        '''
        save_contact method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the user_list
        '''

        User.user_list.remove(self)