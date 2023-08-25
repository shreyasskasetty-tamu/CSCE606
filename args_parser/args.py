from typing import List
import os
import sys
import re
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, ".."))
sys.path.append(parent_directory)
from utility.exceptions import *

class Args:
    def __init__(self, schema : str, args : List[str]):
        """
            Builds the argument parser for the given schema and 
            parses the given arguments; throws an exception on error.
        """
        self.schema = schema
        self.args = args
        self.flags = {} #dictionary map: option -> value
        self.data_specifiers = {} #dictionary map: option -> data_specifier
        self.parse_schema()
        self.parse_arguments()
        
    def parse_schema(self):
        """
            Parses the schema string and stores the data specifiers for each flag
            in a dictionary; throws an exception on parsing error.
        """
        if len(self.schema) == 0:
            return
        schema_options = self.schema.split(",")
        schema_pattern = r"^[a-zA-Z](#|\*?)$"
        for option in schema_options:
            flag = option.strip()
            if not re.match(schema_pattern,flag):
                raise SchemaParseError("Invalid schema format: Valid datatype specifier(*,#,None), Valid Flags: a-z or A-Z)")
            else:
                if len(option) == 1:
                    self.data_specifiers[flag[0]] = None
                else:
                    self.data_specifiers[flag[0]] = flag[1]        

    def parse_arguments(self):
        """
            Parses the arguments with the help of a valid schema and stores the 
            corresponding flag values in a dictionary; throws an exception on parsing error.
        """

        #Parse the arguments for values and check for errors
        for arg in self.args:
            if arg.startswith("-"):
                option = arg[1]
                value = None
                if option in self.data_specifiers:
                    if self.data_specifiers[option] == "#":
                        try:
                            value = int(arg[2:])
                        except ValueError:
                            raise ValueError("Invalid Integer Value")
                    elif self.data_specifiers[option] == "*":
                        value = arg[2:]
                    else:
                        value = True
                else:
                   raise ArgumentParseError("Invalid Argument: Argument not present in schema!")
                self.flags[option] = value
        
        # set the options/flags with default values if its not a part of arguments
        for key in self.data_specifiers.keys():
            if key not in self.flags.keys():
                if self.data_specifiers[key] == None:
                    self.flags[key] = False
                elif self.data_specifiers[key] == "*":
                    self.flags[key] = ""
                elif self.data_specifiers[key] == "#":
                    self.flags[key] = 0        

    def has(self, flag: str) -> bool:
        """
            Returns True iff the specified flag was present in the arguments.
        """
        return flag in self.flags

    def get_boolean(self, flag : str) -> bool:
        """
            Returns the value (expected to be of boolean type) of the specified flag; 
            throws an exception if the flag is not defined by schema to be a boolean.
        """
        if flag not in self.flags:
            raise FlagError("Flag not present in schema")

        if self.data_specifiers[flag] != None:
            raise FlagError("Invalid request. Flag does not have boolean type!")

        return self.flags[flag]

    def get_string(self, flag: str) -> str:
        """
            Returns the value (expected to be of string type) of the specified flag; 
            throws an exception if the flag is not defined by schema to be a string.
        """
        if flag not in self.flags:
            raise FlagError("Flag not present in schema")

        if self.data_specifiers[flag] != "*":
            raise FlagError("Invalid request. Flag does not have string type!")
            
        return self.flags[flag]
    
    def get_integer(self, flag: str) -> int:
        """
            Returns the value (expected to be of integer type) of the specified flag; 
            throws an exception if the flag is not defined by schema to be an integer.
        """
        if flag not in self.flags:
            raise FlagError("Flag not present in schema")

        if self.data_specifiers[flag] != "#":
            raise FlagError("Invalid request. Flag does not have integer type!")

        return self.flags[flag]

