import pyperclip # Impporting the pyperclip module
import string
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
    def generate_password(password):

        '''
        Method to generate a new password
        '''


        # alphabet = string.ascii_letters + string.digits
        # password = ''.join(secrets.choice(alphabet) for i in range(5))
        string = "abcdefghigjkmnopqrstuvwxyz1234567890-_=+{}|"';>./,`!@#$^&*()`'
        account_password = "".join(random.sample(string, int(password)))
        password = account_password
        return password
