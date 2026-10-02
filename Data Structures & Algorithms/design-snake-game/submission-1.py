class Node:

    def __init__(self, pos):
        self.pos = pos
        self.prev = None
        self.next = None
    
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        # 0 - none 1 - food 2 - snake
        self.rows, self.cols = height, width
        self.food = food
        self.head = Node([0, 0])
        self.tail = Node([-1, -1])
        self.head.next, self.tail.prev = self.tail, self.head
        self.score = 0
        self.food_idx = 0

    
    def move(self, direction: str) -> int:
        if not self.food:
            return -1
        dir_map = {"R": [0, 1], "D": [1, 0], "L": [0, -1], "U": [-1, 0]}
        r = self.head.pos[0] + dir_map[direction][0]
        c = self.head.pos[1] + dir_map[direction][1]
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return -1
        if self.food_idx < len(self.food) and [r, c] == self.food[self.food_idx]:
            new_head = Node([r, c])
            new_head.next, self.head.prev = self.head, new_head
            self.head = new_head
            cur = self.head.next
            while cur:
                if self.head.pos == cur.pos:
                    return -1
                cur = cur.next
            self.score += 1
            self.food_idx += 1
            return self.score
        else:
            new_head = Node([r, c])
            new_head.next, self.head.prev = self.head, new_head
            self.head = new_head
            self.tail.prev.prev.next, self.tail.prev = self.tail, self.tail.prev.prev
            cur = self.head.next
            while cur:
                if self.head.pos == cur.pos:
                    return -1
                cur = cur.next
            return self.score
            


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
