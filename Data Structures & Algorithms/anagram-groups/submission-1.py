from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for st in strs:
            count = [0] * 26 #a->z
            for c in st:
                count[ord(c) - ord("a")] += 1 #+=1 to map correctly
                #to figure out letter
            key = tuple(count)
            if key in res:
                res[key].append(st)
            else:
                res[key] =[st]
        return list(res.values())
            
       
    
    
        