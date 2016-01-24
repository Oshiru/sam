###############################################################################
#                                                                             #
#  GLOBALS                                                                    #
#                                                                             #
###############################################################################

from collections import defaultdict

# variables
#
# A dictionary of the variables contained in sam with keys the variable name
# and values being a variable type
#
# TODO implement namespaces via a tree structure

variables = defaultdict()


class Variable(object):

    def __init__(self, name):
        self.name = name


class Int(Variable):

    def __init__(self, name, value):
        Variable.__init__(self, name)
        self.value = value
