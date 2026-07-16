class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            x, y = point
            return x**2 + y**2

        def partition(s, e):
            p = points[e]
            l = s
            for i in range(s, e):
                if dist(points[i]) <= dist(p):
                    points[l], points[i] = points[i], points[l]
                    l += 1
            points[l], points[e] = points[e], points[l]
            return l

        target = k - 1
        s = 0
        e = len(points) - 1
        while s <= e:
            pivot = partition(s, e)
            if pivot < target:
                s = pivot + 1
            elif pivot > target:
                e = pivot - 1
            else:
                return points[ : k]

