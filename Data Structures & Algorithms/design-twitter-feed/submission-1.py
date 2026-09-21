class Twitter:

    def __init__(self):
        self.user_posts = defaultdict(list)
        self.user_follows = defaultdict(set)
        self.post_cnt = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_cnt += 1
        self.user_posts[userId].append([tweetId, self.post_cnt])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        followees = self.user_follows[userId] | {userId}
        maxHeap = []
        heapq.heapify(maxHeap)
        for followee in followees:
            if self.user_posts[followee]:
                heapq.heappush(maxHeap, (-self.user_posts[followee][len(self.user_posts[followee]) - 1][1], followee, self.user_posts[followee][len(self.user_posts[followee]) - 1][0], len(self.user_posts[followee]) - 1))
        while maxHeap and len(res) < 10:
            timestamp, poster, tweetId, tweet_index = heapq.heappop(maxHeap)
            if tweet_index - 1 >= 0:
                heapq.heappush(maxHeap, (-self.user_posts[poster][tweet_index - 1][1], poster, self.user_posts[poster][tweet_index - 1][0], tweet_index - 1))
            res.append(tweetId)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows[followerId].discard(followeeId)
