class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #convert using ord(letter.lower()) - 96
        #just need a count
        #why a heap, for most frequent character use heap
        #only upper case though so maybe easier way to convert
        #more frequent so we aren't as idle
        #no max heap, just use negative
        #use queue for the idle time 
        #each task 1 unit time
        '''
        Hash Maps / Frequency Counting - Used to count occurrences of each task type
        Greedy Algorithms - The optimal solution prioritizes the most frequent tasks first
        Heap / Priority Queue - The efficient solution uses a max-heap to always select the highest-frequency task
        Queue Data Structure - Used to track tasks in cooldown before they can be re-executed
        '''

        '''
        fruit_counts = Counter(my_list)
        print(fruit_counts)
        # Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})
        '''
        counts = Counter(tasks)
        #hashmap
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)
        #turn lsit to heap
        time = 0
        q = deque()
        while maxHeap or q:
            time +=1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
                    #keep track of time and count in queue, figure out if you want to be idle
            if q and q[0][1] == time:
                #first in first out
                heapq.heappush(maxHeap, q.popleft()[0])
        return time



        