# Nodes

current_max_node = 0
precedence = [ASSIGNMENT, DIV, MUL, PLUS, MINUS, INTEGER, VAR, VAR_DEC, INT_DEC]
expected_children = [2, 2, 2, 2, 2, 1, 0, 1, 0]

class NodeStructureException(Exception):
	pass

class NoChildrenException(Exception):
	pass

class Node(object):
	def __init__(self, type):
	    self.type = type
	    self.id = current_max_node + 1
	    self.expected_children = expected_children[precedence.index(self.type)]
	    current_max_node++
	    self.children = []

	def is_higher_precedence(self, second_node):
		return (precedence.index(self.type) > precedence.index(second_node.type))

	def add_child(self, child):
		if (self.children.length < expected_children[self.expected_children]):
			self.children.push(child)
		else:
			raise NodeStructureException

	def last_child(self):
		if self.children.length > 0:
			return self.children[-1]
		else:
			raise NoChildrenException
