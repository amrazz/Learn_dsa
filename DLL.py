class DN:
    def __init__(self, value=0):
        self.value = value
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def print_dll(self):
        if self.head is None:
            print("This linked List is empty!!")
            return
        current = self.head
        while current is not None:
            print(current.value, end=" <---> ")
            current = current.next
        print("NONE")

    def print_ll_rev(self):
        print()
        if self.head is None:
            print("This list is empty!!")
            return
        current = self.head
        while current.next is not None:
            current = current.next
        while current is not None:
            print(current.value, end=" <--> ")
            current = current.prev
        print("NONE")

    def add_when_empty(self, value):
        if self.head is None:
            new_node = DN(value)
            self.head = new_node
        else:
            print("This list is not empty!!")

    def add_begin(self, value):
        new_node = DN(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self, value):
        new_node = DN(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current


dll = DLL()
dll.add_begin(123)
dll.add_begin(343)
dll.add_begin(56)
dll.add_begin(246)
dll.print_dll()
dll.print_dll_rev()
