""" SAM  """

# TODO document APIs between files
# TODO implement sami - the interactive element
# TODO !implement a more general tree structure in the parser
# This will invlove tokens specifting what children they expect and a general
# get children function. Also note that precedence can be implemented by going
# to the right until finding an operator of higher precedence

from collections import defaultdict
from interpreter import *
from lexer import *
from parser import *

###############################################################################
#                                                                             #
#  GLOBALS                                                                    #
#                                                                             #
###############################################################################

# variables
#
# A dictionary of te variables contained in sam with keys the variable name
# and values the variable type
#
# TODO !create variable type
#
# TODO implement namespaces via a tree structure

variables = defaultdict()

def main():
    while True:
        try:
            text = input('sam> ')
        except EOFError:
            break
        if not text:
            continue

        my_lexer = Lexer(text)
        my_parser = Parser(my_lexer)
        my_interpreter = Interpreter(my_parser)
        result = my_interpreter.interpret()
        print(result)


if __name__ == '__main__':
    main()
