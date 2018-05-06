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

    