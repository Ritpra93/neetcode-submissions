class TimeMap:
    #why this is binary seach, since timestamps guranteed to be increasing 
    #for each key
    def __init__(self):
        self.TimeMap = {}
        #intialize hashmap
   

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
            #each key is a blank array
        self.TimeMap[key].append([value, timestamp])
        #now you add the [value, timestamp]
    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.TimeMap.get(key, [])
        #original case where the key doesn't have any value, timestamp
        l, r = 0, len(values) - 1
        #beginning point, end point
        while l <= r:
            m = (l+r) //2
            #do middle in the while loop
            if values[m][1] <= timestamp:
                #to find rightmost timestamp
                res = values[m][0]
                l = m +1
                #same as always with binary left = mid + 1
            else:
                r = m -1
                #right becomes mid -1 
        return res
        
#exact timestamp match is wrong, need largest timestamp less than or equal to query
