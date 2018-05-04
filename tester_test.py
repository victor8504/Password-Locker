import unittest # Importing the unittest module
from tester import User

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

        def test_init(self):
            
            '''
            test_init test case to test if the object is initialized properly
            '''

            self.assertEqual(self.new_user.account_name,"Victor Njuguna")
            self.assertEqual(self.new_user.email_address,"victormoore254@gmail.com") 
            self.assertEqual(self.new_user.password,"victor8504")

if __name__ == '__main__':
    unittest.main()
                        
    