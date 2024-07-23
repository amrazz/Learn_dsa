"""
Linked List
A linked list is a linear data structure, in which the elements are not stored at
contiguous memory locations.The elements in a linked list are linked using pointers 

* Elements can be removed or inserted easily from any position.
* You can implement stack and queue using linked list.
* In real life we can use LL in web browser to go to the previous page using LL
* use in the music player the songs are linked


DISADVANTAGE -->

* Needs extra memory for saving node and data
* Random access is not possible it sould be traversed



DATA&REF  head==▢▢-->▢▢-->▢▢-->▢▢-->▢▢==tail
"""

"""class Node:
    def __init__(self, value=0, next = None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def print_element(self):
        current = self.head
        if current is not None:
            print(current.value, end=" --> ")
            current = current.next
        else:
            print("the list is empty")
        
ll = LinkedList()
list.head = Node(1)
second = Node(2)
third = Node(3)




Three nodes have been created.We have references to these three blocks as head,second and third
 
    list.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | None |     | 2 | None |     | 3 | None |
    +----+------+     +----+------+     +----+------+
    
    
list.head.next = second
second.next = third


Now next of head is refers to second and second Node refers to third. So all three nodes are linked.
 
    list.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | o-------->| 2 | o-------->| 3 | null |
    +----+------+     +----+------+     +----+------+

"""


class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("This linked List is empty!!")
            return
        current = self.head
        while current is not None:
            print(current.value, end=" ---> ")
            current = current.next
        print("NONE")

    def add_begining(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def add_after(self, value, n):
        current = self.head
        while current is not None:
            if current.value == n:
                break
            current = current.next
        if current is None:
            print("The data does not exits!!")
        else:
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node

    def add_before(self, value, n):
        if self.head is None:
            print("This list is empty!!")
            return
        if self.head.value == n:
            self.add_begining(value)
            return
        current = self.head

        while current.next is not None and current.next.value != n:
            current = current.next
        if current.next is None:
            print("Data does not exist!!")
        else:
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node

    def arr_to_ll(self, arr):
        for i in arr:
            self.add_end(i)

    def del_begining(self):
        if self.head is None:
            print("There is nothing to delete")
            return
        self.head = self.head.next

    def del_end(self):
        if self.head is None:
            print("There is nothing to delete!!")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None

    def del_after(self, n):
        if self.head is None:
            print("There is nothing to delete!!")
            return

        current = self.head
        while current is not None and current.value != n:
            current = current.next

        if current is None or current.next is None:
            print("Given value does not exist or has no next node!!")
        else:
            current.next = current.next.next

    def del_before(self, n):
        if self.head is None:
            print("There is nothing to delete!!")
            return
        if self.head.value == n:
            self.head = self.head.next
            return
        current = self.head
        while current.next.next is not None and current.next.next.value != n:
            current = current.next
        if current.next.next is None:
            print("The given value does not exist in the list")
        else:
            current.next = current.next.next

    def to_list(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.value)
            current = current.next
        return elements

    def sorted_list(self):
        elements = self.to_list()
        elements.sort()
        for i in elements:
            print(i, end=" ---> ")
        print("None")

    def reversed_list(self):
        elements = self.to_list()
        for i in elements[::-1]:
            print(i, end=" --> ")
        print("NONE")

    def remove_dup(self):
        if self.head is None:
            print("Linked List is empty!!")
            return
        current = self.head
        while current.next is not None:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next

    def reverse(self):
        head = None
        current = self.head
        while current is not None:
            new_node = Node(current.value)
            new_node.next = head
            head = new_node
            current = current.next
        self.head = head

    def reverse(self):
        head = None
        current = self.head
        while current is not None:
            new_node = Node(current.value)
            new_node.next = head
            head = new_node
            current = current.next
        self.head = head


# l = LinkedList()
# l.add_begining(2222)
# l.add_before(232, 2222)
# l.add_before(64, 2222)
# l.add_before(74, 2222)
# l.add_before(97, 2222)
# l.add_before(44, 2222)
# l.add_after(965, 2222)
# l.add_after(445, 2222)
# l.add_after(943, 2222)
# l.add_after(54, 2222)
# l.add_after(7, 2222)

# print("this is the original ")
# l.print()
# print("this is the sorted list")
# l.sorted_list()
# print("this is the reversed list")
# l.reverse()
# l.print()


# -----------------------------------------------------------------------


class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_last(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            return
        else:
            curr = self.head
            while curr.pointer is not None:
                curr = curr.pointer
            curr.pointer = newnode

    def add_begining(self, value):
        new_node = Node(value)
        new_node.pointer = self.head
        self.head = new_node

    def print(self):
        if self.head is None:
            print("This list is empty!!")
            return
        curr = self.head
        while curr is not None:
            print(curr.value, end=" --> ")
            curr = curr.pointer
        print("NONE")

    def remove(self, value):
        if self.head is not None:
            if self.head.value == value:
                self.head = self.head.pointer
            else:
                curr = self.head
                while curr.pointer is not None and curr.pointer.value != value:
                    curr = curr.pointer
                if curr.pointer is not None:
                    curr.pointer = curr.pointer.pointer


# ll = LinkedList()
# ll.add_last(222)
# ll.add_last(322)
# ll.add_last(111)
# ll.add_last(8)
# ll.add_last(54)
# ll.add_last(309)
# ll.add_last(99)
# ll.add_last(7554)
# ll.print()
# ll.remove(111)
# ll.remove(99)
# ll.print()


data = [
    {"Name": "Danish", "age": 18, "class": "A"},
    {"Name": "Amraz", "age": 17, "class": "B"},
    {"Name": "Asjad", "age": 16, "class": "A"},
    {"Name": "Jasir", "age": 15, "class": "B"},
]

store = {}
for i in data:
    clas = i["class"]
    age = i["age"]

    if clas not in store:
        store[clas] = []
    store[clas].append(age)


avg_age = {}

for clas, age in store.items():
    avg_age[clas] = sum(age) / len(age)

# for cls, avg_age in avg_age.items():
# print(f"Average age for class {cls}: {avg_age:.2f}")
