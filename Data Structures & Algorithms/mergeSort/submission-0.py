# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, l1, l2):
        merged = []
        p1 = 0
        p2 = 0
        for i in range(len(l1) + len(l2)):
            while p1 < len(l1) and p2 < len(l2):
                
                if l1[p1].key > l2[p2].key:
                    merged.append(l2[p2])
                    p2 += 1
                else:
                    merged.append(l1[p1])
                    p1 += 1
        merged.extend(l1[p1 : ])
        merged.extend(l2[p2 : ])
        return merged

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) == 0 or len(pairs) == 1:
            return pairs
        l = 0
        r = len(pairs) - 1
        m = (l + r) // 2
        left = self.mergeSort(pairs[l : m + 1])
        right = self.mergeSort(pairs[m + 1 : r + 1])

        result = self.merge(left, right)

        return result
