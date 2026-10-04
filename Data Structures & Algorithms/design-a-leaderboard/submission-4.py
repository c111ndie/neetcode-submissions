class Leaderboard:

    def __init__(self):
        self.player_score = {}
        self.scores = []
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.player_score:
            self.player_score[playerId] += score
        else:
            self.player_score[playerId] = score
    
    def top(self, K: int) -> int:
        topk_sum = sum(heapq.nlargest(K, self.player_score.values()))
        return topk_sum
        

    def reset(self, playerId: int) -> None:
        self.player_score[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
