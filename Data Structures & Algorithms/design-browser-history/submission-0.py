class Page:

    def __init__(self, url = ""):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Page(homepage)
        self.cur = self.homepage

    def visit(self, url: str) -> None:
        newPage = Page(url)
        newPage.prev = self.cur
        self.cur.next = newPage
        self.cur = newPage

    def back(self, steps: int) -> str:
        if steps == 0:
            return self.cur.url
        for i in range(steps):
            if self.cur.prev == None:
                return self.cur.url
            self.cur = self.cur.prev
        return self.cur.url
        

    def forward(self, steps: int) -> str:
        if steps == 0:
            return self.cur.url
        for i in range(steps):
            if self.cur.next == None:
                return self.cur.url
            self.cur = self.cur.next
        return self.cur.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)