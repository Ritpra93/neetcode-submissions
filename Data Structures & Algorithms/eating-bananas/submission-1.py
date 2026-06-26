class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #important pattern once a speed works, all speed works = another reason why binary search
        #right > left, if ordered could be binary search
        l = 1
        #minimum possible speed
        right = max(piles)
        #max needed speed, we know h < max(piles)
        res = right
        while l <= right:
            k = (l+right) // 2
            #start mid point here first as always

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
                #totalTime += (p + k - 1) // k same thing
            if totalTime <= h :
                #works, but see if there is even a smaller speed
                res = k 
                right= k -1
            else:
                #check right half for a bigger speed, too slow
                l = k + 1
        return res


        