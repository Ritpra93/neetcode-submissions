class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #prerequisites where prerequisites[i] = [a, b]
        #num courses is the nodes 
        #0 to numcourse -1 
        #course have prereqs 
        #course 0 you have to take course 1 first, expressed as pair [0,1] 
        #no outward edges from 0 so can take 0, same with 1
        #not possible [[1,0], [0,1]]
        #dfs for this
        #no pre-reqs are base cases
        #make a hashmap where courses and maps to prereqs
        #dfs [0, n-1]
        #basically checks ie 3 -> [1,2], go to 1 and 2 to check pre-reqs, work backwards
        #O(n+p)

        '''
        numCourses = 4

    prerequisites = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 3]
    ]
    0 -> [1, 2]
1 -> [3]
2 -> [3]
3 -> [], each one has prereq so hashmap makes sense
        '''
        prereqsMap = {i:[] for i in range(numCourses)}
        '''
        what hashmap looks like before courses added
        {
    0: [],
    1: [],
    2: [],
    3: []
}
'''
        for courses, pre in prerequisites:
            #add the prereqs
            prereqsMap[courses].append(pre)

        #courses currently being explored
        visitedSet = set()
        
        def dfs(courses):
            if courses in visitedSet:
                return False
                #checks if cycle
            if prereqsMap[courses] == []:
                return True
                #course doesn't have any other prereqs
            
            visitedSet.add(courses)
            #add course to set
            for pre in prereqsMap[courses]:
                if not dfs(pre):
                    return False
            visitedSet.remove(courses)
                #after all prereqs remove the course
            prereqsMap[courses] = []
                #already checked so don't check again
            return True
        for courses in range(numCourses):
            #go run dfs on all of them now
            if not dfs(courses):
                return False
        return True
        
            