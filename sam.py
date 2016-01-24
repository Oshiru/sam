""" SAM  """

# TODO document APIs between files
# TODO implement sami - the interactive element
# TODO !implement a more general tree structure in the parser
# This will invlove tokens specifting what children they expect and a general
# get children function. Also note that precedence can be implemented by going
# to the right until finding an operator of higher precedence

from sam_interpreter import Interpreter


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
