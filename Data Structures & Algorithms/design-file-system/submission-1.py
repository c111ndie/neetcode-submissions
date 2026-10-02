_MISSING = object()

class FileSystem:

    def __init__(self):
        self.values = {}

    def getParent(self, path):
        for i in range(len(path)-1, 0, -1):
            if path[i] == "/":
                return path[:i]
        return _MISSING

    def createPath(self, path: str, value: int) -> bool:
        parent = self.getParent(path)
        if path in self.values:
            return False
        if parent is _MISSING or parent in self.values:
            self.values[path] = value
            return True
        else:
            return False

    def get(self, path: str) -> int:
        if path in self.values:
            return self.values[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
