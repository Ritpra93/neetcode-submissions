class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        #pointers one at beginning, and one at end
        while l < r:
            #go until left < right, cause if left > right we're repeating
            cursum = numbers[l] + numbers[r]
            if cursum > target:
                #case where target is smaller, so decrement right to get a smaller cursum
                r -= 1
            elif cursum < target:
                l +=1 
                #case where we know we can skip the current left pointer, since smaller than the target
            else:
                return [l+1, r+1]
                #we are always guranteed a solution and we know that there is always only one solution
        