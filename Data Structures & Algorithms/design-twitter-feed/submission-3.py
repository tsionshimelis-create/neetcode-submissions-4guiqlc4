class Twitter:

    def __init__(self):
        # followerId: set(followee)
        self.followings = defaultdict(set)
        # store (time, tweetId, userId) max-heap 
        # since we will be ordering tweets based on the time they were posted
        # we can't use tweet Id's to check recency because tweetId - 3 can 
        # be posted before tweetId - 2
        self.recent_tweets = []
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.recent_tweets, [-self.time, tweetId, userId])
        self.time += 1
        self.follow(userId, userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        feed = []

        while self.recent_tweets:
            tweet = heapq.heappop(self.recent_tweets)
            if tweet[2] in self.followings[userId] and len(news_feed) < 10:
                news_feed.append(tweet[1])
            feed.append(tweet)

        for i in range(len(feed)):
            heapq.heappush(self.recent_tweets, feed[i])
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)


        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followings[followerId] and followeeId != followerId:
            self.followings[followerId].remove(followeeId)
     
        
