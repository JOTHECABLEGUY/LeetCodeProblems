import re
import sys

class Calculator(object):
    def __init__(self):
        self.expression = ""
        self.result = None
        self.valid = False
    def get_result(self):
        self.is_expression_valid()
        try:
            return eval(self.expression)
        except Exception as e:
            print(f"Invalid expression: either the expression results in a denominator equal to 0 or its syntax is incorrect: {self.expression}")
            return sys.maxsize
    def is_expression_valid(self):
        search_for_valid_math_chars = re.compile(r"[\(\)+\-/\*\d]+$").match(self.expression)
        search_for_div_by_0 = re.compile(r"/\(?(\([+\-\d]+\))*([\*\d])*0").search(self.expression)
        
        self.valid = search_for_valid_math_chars is not None and search_for_div_by_0 is None
        
def main():
    calculator = Calculator()
    while True:
        calculator.expression = input("Enter the expression to evaluate using a calculator ('q' to quit): \n")
        if calculator.expression == 'q':
            break
        result = calculator.get_result()
        if result == sys.maxsize:
            print(f"INVALID EXPRESSION: {calculator.expression}! Try again.")
            continue
        print(result)
if __name__ == "__main__":
    main()
    