class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
    
class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return
        cur = self.root
        while True:
            if cur.key > key:
                if not cur.left:
                    cur.left = newNode
                    return
                cur = cur.left
            elif cur.key < key:
                if not cur.right:
                    cur.right = newNode
                    return
                cur = cur.right
            else:
                cur.val = val
                return
            
    def get(self, key: int) -> int:
        if not self.root:
            return -1
        cur = self.root
        while True:
            if cur.key == key:
                return cur.val
            elif cur.key > key:
                if not cur.left:
                    return -1
                cur = cur.left
            else:
                if not cur.right:
                    return -1
                cur = cur.right
                    

    def getMin(self) -> int:
        if not self.root:
            return -1
        res = self.root
        while res.left:
            res = res.left
        return res.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        res = self.root
        while res.right:
            res = res.right
        return res.val


    def remove(self, key: int) -> None:
        def removed(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = removed(node.left, key)
            elif key > node.key:
                node.right = removed(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    cur = node.right
                    while cur.left:
                        cur = cur.left
                    node.key = cur.key
                    node.val = cur.val
                    node.right = removed(node.right, cur.key)
            return node
        self.root = removed(self.root, key)
        

    def getInorderKeys(self) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.key)
            dfs(root.right)
        dfs(self.root)
        return res
