import pyperclip # Impporting the pyperclip module
import random
class Credential:

    '''
    Class that generates new instances of credential
    '''

    credential_list = [] # Empty credential list

    def __init__(self, password, password_length):

        '''
        __init__ method that helps us define properties for our objects.

        Arg:
        password: New credential password.
        '''

        self.password = password
        self.password_length = password_length

    @classmethod
    def generate_password(cls, password_length):

        '''
        Method to generate a new password
        '''

        string = "abcdefghigjkmnopqrstuvwxyz1234567890-_=+{}|"';>./,`!@#$^&*()`'
        account_password = "".join(random.sample(string, int(password_length)))
        password = account_password
        return password
