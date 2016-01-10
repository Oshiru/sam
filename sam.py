""" SAM  """

# TODO document APIs between files
# TODO implement sami - the interactive element
# TODO !implement a more general tree structure in the parser
# This will invlove tokens specifting what children they expect and a general
# get children function. Also note that precedence can be implemented by going
# to the right until finding an operator of higher precedence

from collections import defaultdict
from sam_interpreter import Interpreter

###############################################################################
#                                                                             #
#  GLOBALS                                                                    #
#                                                                             #
###############################################################################

# variables
#
# A dictionary of the variables contained in sam with keys the variable name
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

        my_interpreter = Interpreter(text)
        result = my_interpreter.interpret()
        print(result)


if __name__ == '__main__':
    main()
