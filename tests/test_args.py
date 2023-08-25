import unittest
import os 
import sys
# Add the parent directory (root directory) to the Python path
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, ".."))
sys.path.append(parent_directory)
from args_parser import Args
from utility.exceptions import *

class TestArgsParser(unittest.TestCase):
    def test_has_flag(self):
        """
            Positive Test case to check has option method.
        """
        schema = "l,c#,b*"
        args = ["-l","-c42"]
        arg = Args(schema,args)
        self.assertTrue(arg.has("l"))
    
    def test_invalid_has_flag(self):
        """
            Negative Test case to check has option method.
        """
        schema = "l,c#,b*"
        args = ["-l","-c42"]
        arg = Args(schema,args)
        self.assertFalse(arg.has("z"))

    def test_get_boolean_option(self):
        """
            Positive test case to check get boolean function.
        """
        schema = "l,c#,b*"
        args = ["-l","-c42"]
        arg = Args(schema,args)
        self.assertTrue(arg.get_boolean("l"))
    
    def test_get_boolean_option_default(self):
        """
            Positive test case to check default case of boolean option.
        """
        schema = "l,c#,b*"
        args = ["-c42"]
        arg = Args(schema,args)
        self.assertFalse(arg.get_boolean("l"))

    def test_get_boolean_option_invalid_flag(self):
        """
            Negative test case to check invalid flag passed to get_boolean method.
        """
        schema = "l,c#,b*"
        args = ["-c42"]
        arg = Args(schema,args)
        with self.assertRaises(FlagError):
            arg.get_boolean("e")
    
    def test_invalid_boolean_option(self):
        """
            Negative test case to check get boolean function - non boolean flag is passed to get_boolean method.
        """
        schema = "l,c#,b*"
        args = ["-l","-c42"]
        arg = Args(schema,args)
        with self.assertRaises(FlagError):
            arg.get_boolean("b")

    def test_integer_option(self):
        """
            Positive test case to check get integer option
        """
        schema = "l,c#,b*"
        args = ["-l","-c42"]
        arg = Args(schema,args)
        self.assertEqual(arg.get_integer("c"),42)
    
    def test_invalid_integer_option(self):
        """
            Negative test case to check get integer option - non integer flag is passed to get_integer method.
        """
        schema = "l,c#,b*"
        args = ["-l","-c42"]
        arg = Args(schema,args)
        with self.assertRaises(FlagError):
            arg.get_integer("b")

    def test_invalid_integer_value(self):
        """
            Negative test case to check get integer option - string is passed instead of integer
        """
        schema = "l,c#,b*"
        args = ["-l","-ct"]
        with self.assertRaises(ValueError):
            arg = Args(schema,args)
            arg.get_integer("c")

    def test_get_integer_invalid_flag(self):
        """
            Negative test case to check get integer option with invalid flag
        """
        schema = "l,c#,b*"
        args = ["-l","-bWhoop"]
        arg = Args(schema,args)
        with self.assertRaises(FlagError):
            arg.get_integer("f")

    def test_get_string_option(self):
        """
            Positive test case to check get string option
        """
        schema = "l,c#,b*"
        args = ["-l","-bWhoop"]
        arg = Args(schema,args)
        self.assertEqual(arg.get_string("b"),"Whoop")

    def test_get_string_invalid_flag(self):
        """
            Negative test case to check get string option with invalid flag
        """
        schema = "l,c#,b*"
        args = ["-l","-bWhoop"]
        arg = Args(schema,args)
        with self.assertRaises(FlagError):
            arg.get_string("f")

    def test_invalid_string_option(self):
        """
            Positive test case to check get string option
        """
        schema = "l,c#,b*"
        args = ["-l","-bWhoop"]
        arg = Args(schema,args)
        with self.assertRaises(FlagError):
            arg.get_string("l")
    
    def test_empty_schema(self):
        """
            Positive test case - empty schema
        """
        schema = ""
        args = []
        arg = Args(schema,args)
        pass

    def test_invalid_argument_syntax(self):
        """
            Negative test case - Invalid argument syntax
        """
        schema = "l,b*"
        args = ["-l","b"]
        with self.assertRaises(ArgumentParseError):
            arg = Args(schema,args)

    def test_invalid_schema(self):
        """
            Negative test case to check for invalid schema
        """
        schema = ","
        args = ["-l","-bWhoop"]
        with self.assertRaises(SchemaParseError):
            arg = Args(schema,args)
    
    def test_invalid_data_type(self):
        """
            Nagative test case to check for invalid data type
        """
        schema = "l,c#,b!"
        args = ["-l","-bWhoop"]
        with self.assertRaises(SchemaParseError):
            arg = Args(schema,args)
    
    def test_invalid_args(self):
        """
            Negative test case to check for invalid arguments
        """
        schema = "l,c#,b*"
        args = ["-l","-e"]
        with self.assertRaises(ArgumentParseError):
            arg = Args(schema,args)


if __name__ == "__main__":
    unittest.main()