###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################

from sam_parser import Parser
from sam_token import *

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, text):
        self.parser = Parser(text)

    def type_error(self, node):
        raise Exception("No visit_{} method".format(node.type))

    def interpret_tree(self, tree):
        """interpret_tree: performs the calculations implied
        by the given tree"""

        def recurse(node):
            for child in node.children:
                recurse(child)
            interpret_node(node)

        recurse(tree.root)
        return None


    def interpret_node(self, node):
        """ interpret_node: interperts a given node. Note that this function
        assumes that all the children of the node are present"""
        method_name = "interpret_" + node.type
        method_to_call = getattr(self, method_name, self.type_error)
        return method_to_call(node)

    def interperet_INTEGER(self, node):
        pass

    def interperet_PLUS(self, node):
        node.type = INTEGER
        node.value =

    def interpret(self):
        self.parser.parse()
        return interpret_tree(self.parser.tree)
