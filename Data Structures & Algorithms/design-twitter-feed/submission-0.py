class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) #userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) #user id-> set of followeeId
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        #queue fifo?
        #these difficult 
        #use min heap, negatives as always since no max heap in python
        #hashmap user id -> lsit of [count, tweetid]
        #pointer at end since that will be the most recent
        #but optimal is using min Heap, but doesn't change time complexity much
        res = []
        minHeap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                #make sure they really do have a tweet
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        #now do min heap
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index -1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        #follower id is following followeeid, hashmap makes sense
        #map user id -? List of followeeId, just keep adding
        #hash set makes more sense since unique
        self.followMap[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #just need a hashset
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
