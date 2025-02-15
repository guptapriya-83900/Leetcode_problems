import heapq
class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list)
        self.following=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap=[]
        for tweet in self.tweets[userId]:
            heapq.heappush(minHeap,tweet)

        for followee in self.following[userId]:
            for tweet in self.tweets[followee]:
                heapq.heappush(minHeap, tweet)


        return [tweetId for _, tweetId in heapq.nlargest(10, minHeap)]


    def follow(self, followerId: int, followeeId: int) -> None:
         if followerId != followeeId:  
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId) 
        
