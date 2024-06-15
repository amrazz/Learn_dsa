class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current is not None:
            print(current.value, end=" --> ")
            current = current.next
        print("NONE")

    def delete(self, target):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current.next is not None and current.next.value != target:
            current = current.next
        if current is None:
            print("Not found")
        else:
            current.next = current.next.next

    def mid(self):
        if self.head is None:
            print("List is empty")
            return

        # Step 1: Find the length of the list
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next

        # Step 2: Calculate the middle index
        mid = length // 2

        # Step 3: Iterate again to delete the middle node
        count = 0
        current = self.head
        prev = None
        while current is not None:
            if count == mid:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                break
            prev = current
            current = current.next
            count += 1


l = LinkedList()
l.add_begin(10)
l.add_begin(20)
l.add_begin(30)
l.add_begin(40)
l.add_begin(50)
l.mid()
l.print()
