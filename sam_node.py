# Nodes

from sam_token import *
from collections import defaultdict

# precedence - lowest to highest
precedence = [PLUS, MINUS, DIV, MUL, ASSIGNMENT, INTEGER, VAR, INT_DEC]

expected_children = {}

expected_children[ASSIGNMENT] = 2
expected_children[DIV] = 2
expected_children[MUL] = 2
expected_children[PLUS] = 2
expected_children[MINUS] = 2
expected_children[INTEGER] = 0
expected_children[VAR] = 0
expected_children[INT_DEC] = 1


class NodeStructureException(Exception):
    pass

class NoChildrenException(Exception):
    pass

class Node(Token):

    def __init__(self, Token):
        self.type = Token.type
        self.value = Token.value
        self.children = []

    def is_higher_precedence(self, second_node):
        return precedence.index(self.type) > precedence.index(second_node.type)

    def add_child(self, child):
        if len(self.children) < expected_children[self.type]:
            self.children.append(child)
        else:
            raise NodeStructureException

    def last_child(self):
        if len(self.children) > 0:
            return self.children[-1]
        else:
            raise NoChildrenException

    def __str__(self):
        return "Node({})".format(self.type)

    # TODO do __str__ and __repr__
