class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos,spe] for pos, spe in zip(position, speed)]
        #zip kinda like a hashmap for two arrays, but in array format and pairing operation
        '''
        [
        [10,2],
        [8,4],
        [0,1]
        ]
        '''
        '''
        otherwise...
        pair = []
        for i in range(len(position)):
                pair.append([position[i], speed[i]])
        '''
        stack = []
        for pos, spe in sorted(pair)[::-1]:
            #reverse, because car closest affects all the other cars
            stack.append((target-pos) / spe)
            #calculation of when car reaches
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                #[1,7,12]
                '''
                Fleet 1 arrives in 1 hour
                Fleet 2 arrives in 7 hours
                Fleet 3 arrives in 12 hours
                '''
                stack.pop()
                #pop if they merge
        return len(stack)