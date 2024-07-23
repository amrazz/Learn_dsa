class Node:
    def __init__(self, name, age, id) -> None:
        self.info = {"Name": name, "Age": age, "ID": id}
        self.left = None
        self.right = None


class GYM_MANAGEMENT:
    def __init__(self) -> None:
        self.root = None

    def add(self, name, age, id):
        if not name or not age or not id:
            print("All fields are required!!")
            return
        if not self.root:
            self.root = Node(name, age, id)
            print("Member added to the log")
            return
        self.recursive_add(name, age, id, self.root)

    def recursive_add(self, name, age, id, node):
        if id < node.info["ID"]:
            if not node.left:
                node.left = Node(name, age, id)
            else:
                self.recursive_add(name, age, id, node.left)
        elif id > node.info["ID"]:
            if not node.right:
                node.right = Node(name, age, id)
            else:
                self.recursive_add(name, age, id, node.right)

    def display(self):
        if not self.root:
            print("No members in the log")
            return
        result = []
        self.inorder(self.root, result)
        for member in result:
            print(f"ID: {member['ID']}, Name: {member['Name']}, Age: {member['Age']}")

    def inorder(self, node, result):
        if not node:
            return None
        self.inorder(node.left, result)
        result.append(node.info)
        self.inorder(node.right, result)

    def search(self, id):
        return self.recursive_search(id, self.root)

    def recursive_search(self, id, node):
        if not node:
            return None
        if id == node.info["ID"]:
            return node
        if id < node.info["ID"]:
            return self.recursive_search(id, node.left)
        elif id > node.info["ID"]:
            return self.recursive_search(id, node.right)

    def remove(self, id):
        self.root = self.recursive_remove(id, self.root)

    def recursive_remove(self, id, node):
        if not node:
            return node
        if id < node.info["ID"]:
            node.left = self.recursive_remove(id, node.left)
        elif id > node.info["ID"]:
            node.right = self.recursive_remove(id, node.right)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            min_value_node = self.find_min(node.right)
            node.info = min_value_node.info
            node.right = self.recursive_remove(min_value_node.info["ID"], node.right)
        return node

    def find_min(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr

    def update_member(self, id, name=None, age=None):
        node = self.search(id)
        if node:
            if name:
                node.info["Name"] = name
            if age:
                node.info["Age"] = age
            print("User is updated")
        else:
            print("User with this id not found!!")


gym = GYM_MANAGEMENT()
gym.add("Amraz", 19, 1)
print()
gym.add("Asjad", 19, 2)
print()
gym.display()
print()
gym.remove(1)
gym.display()
print()
gym.update_member(2, name="Asjad PK", age=20)
gym.display()
