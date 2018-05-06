import unittest # Importing the unittest module
from tester import User #Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    
    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        
        '''
        Set up method to run before each test cases
        '''

        self.new_account = User("Victor Njuguna", "victormoore254@gmail.com", "victor8504") # create user object

    def tearDown(self):
        
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.user_list = []
    
    def test_init(self):
        
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Victor Njuguna")
        self.assertEqual(self.new_account.email_address,"victormoore254@gmail.com") 
        self.assertEqual(self.new_account.password,"victor8504")

    def test_save_account(self):
        
        '''
        test_save_account test case to test if the account object is saved into
        the user list
        '''

        self.new_account.save_account() # saving the new account
        self.assertEqual(len(User.user_list),1) 

    def test_save_multiple_account(self):

        '''
        test_save_multiple_account to check if we can save multiple account
        objects to our user_list
        '''

        self.new_account.save_account()
        test_account = User("Michy Bats", "michybats@gmail.com", "michybats") # new account
        test_account.save_account()
        self.assertEqual(len(User.user_list),2)

    def test_delete_account(self):
        
        '''
        test_delete_account to test if we can remove an account from our user_list
        '''

        self.new_account.save_account()
        test_account = User("Michy Bats", "michybats@gmail.com", "michybats") # new account
        test_account.save_account()

        self.new_account.delete_account() # Deleting an account object
        self.assertEqual(len(User.user_list),1)

    def test_find_account_by_account_name(self):

        '''
        test to check if we can find an account by account_name and display information
        '''

        self.new_account.save_account()
        test_account = User("Michy Bats", "michybats@gmail.com", "michybats") # new account
        test_account.save_account()

        found_account = User.find_by_account_name("Michy Bats")

        self.assertEqual(found_account.email_address,test_account.email_address)
if __name__ == '__main__':
    unittest.main()
                        
    