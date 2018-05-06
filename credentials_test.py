import pyperclip # Impporting the pyperclip module
import unittest # Importing the unittest module
from credentials import Credential #Importing the credential class

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.
    
    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        
        '''
        Set up method to run before each test cases
        '''

        self.new_password = Credential("victor8504", "10") # create credential object

    def tearDown(self):
        
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Credential.credential_list = []

    def test_init(self):
        
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.password,"victor8504")
        self.assertEqual(self.new_password.password_length,"10")

    # def test_password_generator(self):

    #     """
    #     test_password_generator test case to test if the password generator will work properly.
    #     """

    #     self.new_password.save_password()
    #     random_password = self.new_password.password_gen("17")
    #     self.assertNotEqual(random_password, self.new_profile.account_password) 

if __name__ == '__main__':
    unittest.main() 
                        
        