class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.rows = height
        self.cols = width
        self.food = deque(food)
        self.snake = deque([[0, 0]])
        self.snake_rec = set([(0, 0)])
        self.score = 0

    def move(self, direction: str) -> int:
        dir_map = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}
        head = self.snake[-1]
        new_head = [head[0] + dir_map[direction][0], head[1] + dir_map[direction][1]]
        if not (0 <= new_head[0] < self.rows and 0 <= new_head[1] < self.cols):
            return -1 
        if self.food and new_head == self.food[0]:
            if tuple(new_head) in self.snake_rec:
                return -1
            self.snake.append(new_head)
            self.snake_rec.add(tuple(new_head))
            self.score += 1
            self.food.popleft()
            return self.score
        else:
            to_be_remove = tuple(self.snake.popleft())
            self.snake_rec.remove(to_be_remove)
            if tuple(new_head) in self.snake_rec:
                return -1
            self.snake.append(new_head)
            self.snake_rec.add(tuple(new_head))
            return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
