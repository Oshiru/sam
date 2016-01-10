# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
# TODO make a dictionary with some of the tokens (e.g. '+', '-' etc)
# This should avoid having many ifs in the Lexer
# IDEA maybe this should be in its own file
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF, INT_DEC, VAR, ASSIGNMENT = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF', 'INT_DEC', 'VAR',
    'ASSIGNMENT'
)


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()
