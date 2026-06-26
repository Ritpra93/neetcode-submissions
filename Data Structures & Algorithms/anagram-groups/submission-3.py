class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #hashmap/dict to store values of tuple of character frequency and string
        for string in strs:
            #go through string
             count = [0] * 26
             #intialize count array with 26 for each char
             for c in string:
                count[ord(c) - ord('a')] += 1
                #math that figues out what index to increment count wise
             res[tuple(count)].append(string)
             #make count a tuple and use it as a key, since to make safe to use as keys
        return list(res.values())

    
        
        
        



        