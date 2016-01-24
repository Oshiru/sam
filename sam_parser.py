###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################

# TODO !implement variable declaration and initalisation
from sam_lexer import Lexer
from sam_token import *
from sam_globals import variables

class Tree(object):
    """ Tree class

    Made up of Nodes.

    The job of the parser is to create trees from the Lexer.
    These are then passed to the interpreter."""
    def __init__(self):
        self.root = Node()

    def add_node(self, node_to_add):
        current_node = self.root
        while !current_node.is_null:
            if node_to_add.is_higher_precedence(current_node):
                # Add node at this point
                if current_node == self.root:
                    # Add node at the top
                    try:
                        node_to_add.add_child(self.root)
                    except NodeStructureException:
                        print("NodeStructureException")
                    self.root = node_to_add
                else:
                    # Make node_to_add a child of current_node
                    try:
                        current_node.add_child(node_to_add)
                    except NodeStructureException:
                        print("NodeStructureException")
                break
            # Go to next node
            try:
                current_node = current_node.last_child()
            except NoChildrenException:
                print("This node has no children")


class Parser(object):
    def __init__(self, text):
        self.my_lexer = Lexer(text)
        # set current token to the first token taken from the input
        self.current_token = self.my_lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def create_tree(self):
        """ create_tree: creates a tree from the Lexer"""
        while current_token.type != EOF:
            self.add_node(Node(current_token.type))



    def parse(self):
        """ parse: creates Trees from the Lexer"""
        # TODO add support for multiple trees
        # The parser will maintain a list of trees
        self.tree = self.create_tree()
