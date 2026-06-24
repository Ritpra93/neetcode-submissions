class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        #set the lowest point in array
        high = len(nums) - 1
        #set the highest point in array
        while low <= high:
            mid = (low + high) // 2
            #figure out mid even if not even
            if nums[mid] == target:
                return mid
                #you know its middle
            elif nums[mid] < target:
                low = mid + 1
                #low = mid +1 takes you to the right of arr since greater
            else:
                high = mid - 1
                #takes you to the left of array
        return -1
         