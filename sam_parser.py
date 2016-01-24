###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################

# TODO !implement variable declaration and initalisation
from sam_lexer import Lexer
from sam_node import *  # HACK get rid of *
from sam_token import *
from sam_globals import variables


class Tree(object):
    """ Tree class

    Made up of Nodes.

    The job of the parser is to create trees from the Lexer.
    These are then passed to the interpreter."""

    def __init__(self):
        self.root = None
        pass

    def make_child(self, parent, child):
        try:
            parent.add_child(child)
        except NodeStructureException:
            print("NodeStructureException. Parent: {}".format(parent))

    def add_node(self, new_node):
        if self.root is None:
            # Case where tree is empty
            self.root = new_node
            return None

        if self.root.is_higher_precedence(new_node):
            # Case where the new node should be the root
            self.make_child(new_node, self.root)
            self.root = new_node
            return None

        # Get to the place where the node should be added
        current_node = self.root
        while len(current_node.children) == expected_children[current_node.type]:
            current_node = current_node.last_child()

        # Add node to the bottom of the tree
        self.make_child(current_node, new_node)
        return None

    def __str__(self):
        def print_from_node(node, level=0):
            ret = "\t" * level + repr(node.type) + "\n"
            for child in node.children:
                ret += print_from_node(child, level + 1)
            return ret

        if self.root is not None:
            return print_from_node(self.root)
        else:
            return "Empty tree"


class Parser(object):

    def __init__(self, text):
        self.lexer = Lexer(text)
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def create_tree(self):
        """ create_tree: creates a tree from the Lexer"""
        self.tree = Tree()
        while self.current_token.type != EOF:
            self.tree.add_node(Node(self.current_token))
            self.current_token = self.lexer.get_next_token()
        print(self.tree)

    def parse(self):
        """ parse: creates Trees from the Lexer"""
        # TODO add support for multiple trees
        # The parser will maintain a list of trees
        self.create_tree()
