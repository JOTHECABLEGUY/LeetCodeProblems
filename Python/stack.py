import re
from typing import Union
class Stack(object):
    def __init__(self):
        self.data = []
    def push(self, elem:object):
        self.data.append(elem)
    def pop(self) -> object:
        return self.data.pop(-1)
    def to_string(self) -> str:
        return " ".join(self.data)
    def to_list(self) -> list:
        return self.data
    def is_empty(self):
        return not self.data
def main():
    stack = Stack()
    while (True):
        new_element:Union[str,float] = input("add a new number to the stack, q to quit\n")
        if new_element == 'q':
            break
        if re.match(r"\d+\.*\d*", str(new_element)):
            new_element = float(new_element)
        stack.push(new_element)
    print(stack.to_string())
    print(stack.to_list())
if __name__ == "__main__":
    main()