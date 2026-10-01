class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}
        self.idx = []
        self.cnt = 0

    def insert(self, val: int) -> bool:
        if val not in self.val_to_idx:
            self.idx.append(val)
            self.val_to_idx[val] = self.cnt
            self.cnt += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_to_idx:
            i = self.val_to_idx[val]
            replace = self.idx[-1]
            self.idx[i] = replace
            self.val_to_idx[replace] = i
            self.cnt -= 1
            self.idx.pop()
            self.val_to_idx.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.idx)    
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()