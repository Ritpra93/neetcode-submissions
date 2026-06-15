class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            #early exit case
        s1Count, s2Count = [0] * 26, [0] * 26
        #2 arrays with 26 0's to figure out how many have occoured at a certain time
        #can use hashmap too lol, easier to index with array tho
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            #ord turns letter to number, ie a is 97, ord s1[i] might be c which is 99, 99 - 97 = 2
            s2Count[ord(s2[i]) - ord('a')] += 1
            #same thing for first window of string 2
        matches = 0
        for i in range(26):
           if s1Count[i] == s2Count[i]:
                    matches += 1
            #increment if match
        l = 0 
        #have a left pointer
        for r in range(len(s1), len(s2)):
            #counted first window already so (2, length s2)
            if matches == 26:
                #we match based on positions of arrays like this 
                '''
                a: 1 == 1
                b: 1 == 1
                c: 0 == 0
                d: 0 == 0
                ...
                z: 0 == 0
                '''
                return True
            index = ord(s2[r]) - ord('a')
            #add new character to array w inde
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
                
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
                #no longer matches, remove, how to move the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
                #same method here as before
            l += 1
        return matches == 26
  



        