# STACK

"""
STACK:- Stack is an ordered collection of items where the addition of new items and the removal of items always takes place at the same end.
Stack store items like First In Last Out (FILO) or Last in First Out (LIFO)

stack has 4 methods 
1.Push :- It is used to add elements at the top.
2.pop :- It is used to remove element from the top.
3.Peek or top :- Used to access the element at the top.
4.Isempty :-tells you whether the stack is empty or not.
"""

"""
Stack OverFlow: when the stack exeeds the limit and overflow
"""


"""STACK IMPLEMENTATION"""

# stack = []

# def push():
#     if limit == len(stack):
#         print("You have reached the limit !!!")
#     else:
#         print("Enter an element to add to the stack.")
#     try:
#         element = int(input())
#         stack.append(element)
#         print(f"{element} added to stack")
#         print(f"new stack :{stack}")
#     except ValueError:
#         print("Please enter a valid integer.")

# def pop():
#     if stack:
#         e = stack.pop()
#         print(f"Removed the element: {e}")
#         print("new stack:", stack)
#     else:
#         print("The stack is empty!")


# print("enter the limit of the stack.")
# limit = int(input())
# while True:
#     print("Choose an operation to perform: 1: PUSH, 2: POP, 3: EXIT")
#     choice = int(input())
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop()
#     elif choice == 3:
#         break
#     else:
#         print("Please enter a valid choice (1, 2, or 3)!")
#     print("Please enter a valid integer.")


"""
Ways to implement stack :-

1. from collections --> deque
2. from queue --> LifoQueue
"""


"""       from collections import deque           """

# from collections import deque

# stack = deque()
# stack.append(29)
# stack.append(3454)
# stack.append(45)
# stack.append(3)

# stack.pop()
# stack.pop()
# stack.pop()


"""       from queue import Lifoqueue           """

# from queue import LifoQueue


# stack = LifoQueue(1)
# stack.put(354)
# stack.get()
# stack.get(timeout=3)

# elements = list(stack.queue)
# print(elements)


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

        else:
            return "Stack is empty!!"


def reverse_string(string):
    stack = Stack()

    for i in string:
        stack.push(i)

    rev_str = ""

    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


string = "This is a new born baby!!"
print(reverse_string(string))
