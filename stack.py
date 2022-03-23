from typing import List

class Stack:

    def __init__(self) -> None:
        self.stack: list = []

    def _push_into_stack(self) -> None:
        element = int(input("Enter the element to be pushed into the stack\n"))
        self.stack.append(element)

    def _pop_from_stack(self) -> None:
        if self.stack:
            self.stack.pop()
        else:
            print("\nstack is empty\n")

    def _peek_from_stack(self) -> None:
        if self.stack:
            print("\n",self.stack[-1], "\n")
        else:
            print("\nstack is empty\n")

    def _display_stack(self) -> None:
        if self.stack:
            print("\n".join(list(map(str, self.stack))))
        else:
            print("\nstack is empty\n")

    def __call__(self):
        while True:
            print("1. push into stack\n2. pop from stack\n3. peek from stack\n4. display stack\n")
            choice = input("Enter your choice\n")
            
            if choice == "1":
               self._push_into_stack()
            elif choice == "2":
                self._pop_from_stack()
            elif choice == "3":
                self._peek_from_stack()
            elif choice == "4":
                print("\nBelow are the elements in the stack\n")
                self._display_stack()
                print("\n")
            else:
                break

obj = Stack()
obj()