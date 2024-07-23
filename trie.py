class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def display(self, depth=0, node=None):
        if not node:
            node = self.root

        for char, child in node.children.items():
            end = "END" if child.is_end else ""
            print(" " * (depth * 2), char, end)
            self.display(depth + 1, child)

    def add(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def remove(self, word):
        if not self.search(word):
            print("Word not found!!")
            return
        curr = self.root
        stack = []
        for w in word:
            stack.append(curr)
            curr = curr.children[w]
        curr.is_end = False

        while len(stack) > 1:
            node = stack.pop()
            char = word[len(stack)]

            if not node.children[char].is_end and not node.children[char].children:
                del node.children[char]
            else:
                break
        print("Node removed")

    def suggestions(self, word):
        def dfs(node, path, result):
            if node.is_end:
                result.append("".join(path))
            for char, child in node.children.items():
                dfs(child, path + [char], result)

        curr = self.root
        for char in word:
            if char not in curr.children:
                return []
            curr = curr.children[char]
        result = []
        dfs(curr, list(word), result)
        return result


# Example usage
t = Trie()
t.add("APPLE")
t.add("PINAPPLE")
t.add("APP")
t.add("ELEPHANT")
t.display()
print(t.suggestions("APP"))
