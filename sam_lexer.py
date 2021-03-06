###############################################################################
#                                                                             #
#  LEXER                                                                      #
#                                                                             #
###############################################################################

# This file takes each line of input and returns a list of tokens.
# The key function is get_next_token.

from sam_token import *


class Lexer(object):

    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.current_vars = []

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.previous_char = self.current_char
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def alphanumeric(self):
        """Return a string."""
        string = self.current_char
        self.advance()
        while self.current_char is not None and self.current_char.isalnum():
            string += self.current_char
            self.advance()
        return string

    def get_token_from_string(self, string):
        """Returns the correct token for a specific string"""

        if string == 'int':
            return Token(INT_DEC, string)
        else:
            if (string not in self.current_vars) and (self.token.type == INT_DEC):
                self.current_vars.append(string)
            elif (self.token.type == INT_DEC) or (string not in self.current_vars):
                self.error()

            return Token(VAR, string)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            elif self.current_char.isdigit():
                self.token = Token(INTEGER, self.integer())
                return self.token

            elif self.current_char.isalpha():
                self.token = self.get_token_from_string(self.alphanumeric())
                return self.token

            else:
                current = self.current_char
                self.advance()
                self.token = Token(static_tokens[current], current)
                return self.token

            self.error()

        return Token(EOF, None)
