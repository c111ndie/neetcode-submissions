class TrieNode:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.value = -1

class FileSystem:

    def __init__(self):
        self.root = TrieNode("")

    def createPath(self, path: str, value: int) -> bool:
        components = path.rsplit("/")
        name = components[-1]
        cur = self.root
        for i in range(1, len(components)-1):
            if components[i] in cur.children:
                cur = cur.children[components[i]]
                continue
            else:
                return False
        if name in cur.children:
            return False
        cur.children[name] = TrieNode(name)
        cur.children[name].value = value
        return True
        

    def get(self, path: str) -> int:
        
        components = path.rsplit("/")
        cur = self.root
        for i in range(1, len(components)):
            if components[i] in cur.children:
                cur = cur.children[components[i]]  
            else:
                return -1
        return cur.value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
