import re
import sys
class Calculator(object):
    def __init__(self):
        self.expression = ""
        self.result = None
        self.valid = False
    def get_result(self):
        self.is_expression_valid()
        return eval(self.expression) if self.valid else sys.maxsize
    def is_expression_valid(self):
        if re.match(r"[\(\)\+\-/\*!0-9]+", self.expression) is not None:
            self.valid = True
        self.valid = False
        
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
    