class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp problem where you try all the possibilities
        #add extra 0 so easier to tell what end is, since last stair is not cost[-1], it'll be the top staircase
        cost.append(0)
        for i in range(len(cost) -3 , -1, -1):
            #go backwards to figure out cost[i+1], cost[i+2]
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
            #take the cheapest cost either 1 jump or 2
        return min(cost[0], cost[1])
        #you can start at 0 or 1 index as bottom stair

        