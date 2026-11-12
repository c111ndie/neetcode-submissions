class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_prefix = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if len(self.min_prefix) > 0:
            self.min_prefix.append(min(self.min_prefix[-1], val))
        else:
            self.min_prefix.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.min_prefix.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_prefix[-1]
