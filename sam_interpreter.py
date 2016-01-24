###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################

from sam_parser import Parser
from sam_token import *


class Interpreter(object):

    def __init__(self, text):
        self.parser = Parser(text)

    def type_error(self, node):
        raise Exception("No interpret_{} method".format(node.type))

    def interpret_node(self, node):
        """ interpret_node: interperts a given node. Note that this function
        assumes that all the children of the node are present"""

        method_name = "interpret_" + node.type
        method_to_call = getattr(self, method_name, self.type_error)
        return method_to_call(node)

    def interpret_tree(self, tree):
        """interpret_tree: performs the calculations implied
        by the given tree"""

        def recurse(node):
            for child in node.children:
                recurse(child)
            self.interpret_node(node)

        recurse(tree.root)

    def interpret_INTEGER(self, node):
        pass

    def interpret_PLUS(self, node):
        node.type = INTEGER
        left_child = node.children[0]
        right_child = node.children[1]
        node.value = left_child.value + right_child.value

    def interpret_MINUS(self, node):
        node.type = MINUS
        left_child = node.children[0]
        right_child = node.children[1]
        node.value = left_child.value - right_child.value

    def interpret_MUL(self, node):
        node.type = MUL
        left_child = node.children[0]
        right_child = node.children[1]
        node.value = left_child.value * right_child.value

    def interpret_DIV(self, node):
        node.type = INTEGER
        left_child = node.children[0]
        right_child = node.children[1]
        node.value = left_child.value / right_child.value

    def interpret(self):
        self.parser.parse()
        self.interpret_tree(self.parser.tree)
        return self.parser.tree.root.value
