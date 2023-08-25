from typing import List

class Args:
    def __init__(self, schema : str, args : List[str]):
        """
            Builds the argument parser for the given schema and 
            parses the given arguments; throws an exception on error.
        """
        self.schema = schema
        self.args = args
        self.flags = {}
        self.data_specifiers = {}
        self.parse_schema()
        self.parse_arguments()
        
    def parse_schema(self):
        """
            Parses the schema string and stores the data specifiers for each flag
            in a dictionary; throws an exception on parsing error.
        """
        pass

    def parse_arguments(self):
        """
            Parses the arguments with the help of a valid schema and stores the 
            corresponding flag values in a dictionary; throws an exception on parsing error.
        """
        pass

    def has(self, flag: str) -> bool:
        """
            Returns True iff the specified flag was present in the arguments.
        """
        pass

    def get_boolean(self, flag : str) -> bool:
        """
            Returns the value (expected to be of boolean type) of the specified flag; 
            throws an exception if the flag is not defined by schema to be a boolean.
        """
        pass

    def get_string(self, flag: str) -> str:
        """
            Returns the value (expected to be of string type) of the specified flag; 
            throws an exception if the flag is not defined by schema to be a string.
        """
        pass
    
    def get_integer(self, flag: str) -> int:
        """
            Returns the value (expected to be of integer type) of the specified flag; 
            throws an exception if the flag is not defined by schema to be an integer.
        """
        pass

