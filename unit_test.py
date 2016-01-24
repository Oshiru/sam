from collections import defaultdict
from sam_interpreter import Interpreter
import traceback

failed_tests = {}
passed_tests = []

# Check declaration of a integer.


def declaration_test1():
    try:
        text = "int number = 10;"
        my_interpreter = Interpreter(text)
        result = my_interpreter.interpret()
        #assert(result == "")
        passed_tests.push("declaration_test1")
    except:
        failed_tests[
            "declaration_test1"] = traceback.format_exc().split("\n")[-2]


def main():
    declaration_test1()
    print("Failed Tests:\n")
    for test in failed_tests:
        print(str(test) + ": " + str(failed_tests[test]) + "\n")

    print("Passed Tests:\n")
    for test in passed_tests:
        print(str(test) + "\n")

if __name__ == '__main__':
    main()
