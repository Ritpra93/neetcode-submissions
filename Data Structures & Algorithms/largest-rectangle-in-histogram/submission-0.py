class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            #need both index and height since we wouldn't be able to compute without it
            start = i
            while stack and stack[-1][1] > h:
                #while top height > current height
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                #i - index gives us width of current area, find max of all areas we've computed
                start = index 
                #to figure out how far we can go back to calculate area
            stack.append((start, h))
            #keep both 
        for i, h in stack:
            #some remain cause they never had a bar smaller to their right
            #gotta find right boundary
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
        