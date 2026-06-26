class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #hashmap/dict to store values of sorted string and string
        for string in strs:
            sortedString = "".join(sorted(string))
            #sort string
            res[sortedString].append(string)
            #append string and sorted as key
        return list(res.values())
        #since sorted now its grouped

    
        
        
        



        