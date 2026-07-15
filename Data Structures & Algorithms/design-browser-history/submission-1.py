class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.history.append(homepage)
        self.cur = 0

    def visit(self, url: str) -> None:
        if self.history:
            if self.cur < len(self.history) - 1:
                for i in range(len(self.history) - self.cur - 1):
                    self.history.pop()
            self.history.append(url)
            self.cur += 1

    def back(self, steps: int) -> str:
        if steps == 0:
            return self.history[self.cur]
        for i in range(steps):
            if self.cur == 0:
                return self.history[0]
            self.cur -= 1
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        if steps == 0:
            return self.history[self.cur]
        for i in range(steps):
            if self.cur == len(self.history) - 1:
                return self.history[self.cur]
            self.cur += 1
        return self.history[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)