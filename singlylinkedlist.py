class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertAfterMiddle(self, data):
        new_node = Node(data)
        fast = self.head
        slow = self.head
        if self.head is None:
            self.head = new_node
            return
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        new_node.next = slow.next
        slow.next = new_node

    def insertBeforeMiddle(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        fast = self.head
        slow = self.head
        prev = None
        while fast.next and fast.next.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = new_node
        new_node.next = slow

    def removeDupli(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current.next:
            second = current
            while second.next:
                if current.data == second.next.data:
                    second.next = second.next.next
                if second.next:
                    second = second.next
            current = current.next
        self.printList()

    def delete(self, data):
        current = self.head
        while current.next:
            if self.head.data == data:
                if self.head.next:
                    self.head = self.head.next
                else:
                    self.head = None
            if current.next.data == data:
                if current.next.next:
                    current.next = current.next.next
                else:
                    current.next = None
            if current.next:
                current = current.next
        self.printList()

    def newDelete(self, data):
        while self.head.data == data:
            if self.head.data == data:
                self.head = self.head.next
        node = self.head
        while node.next:
            if node.next.data == data:
                node.next == node.next.next
            node = node.next
        self.printList()

    def listToLinked(self, linked_list, insert_list):
        for i in insert_list:
            linked_list.insertAtEnd(i)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


new_list = LinkedList()
new_list.insertAtBeginning(5)
new_list.insertAtBeginning(6)
new_list.insertAtBeginning(7)
new_list.insertAtBeginning(5)
new_list.insertAtBeginning(5)
new_list.insertAtBeginning(6)
new_list.insertAtBeginning(6)
new_list.printList()
new_list.delete(6)
new_list.newDelete(5)


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def printLinkedList(self):
        if self.head is None:
            print("Add any value to list to print it")
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
