import unittest
import os 
import sys
# Add the parent directory (root directory) to the Python path
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, ".."))
sys.path.append(parent_directory)
from args_parser import Args

class TestArgsParser(unittest.TestCase):
    def test_has_flag(self):
        """
            Test case to check has option method.
        """
        

    def test_boolean_option(self):
        """
            Positive test case to check get boolean function.
        """
        pass
    
    def test_integer_option(self):
        """
            Positive test case to check get integer option
        """
        pass

    def test_string_option(self):
        """
            Positive test case to check get string option
        """
        pass

    def test_invalid_schema(self):
        """
            Negative test case to check for invalid schema
        """
        pass
    
    def test_invalid_data_type(self):
        """
            Nagative test case to check for invalid data type
        """
        pass
    
    def test_invalid_args(self):
        """
            Negative test case to check for invalid arguments
        """
        pass

if __name__ == "__main__":
    unittest.main()