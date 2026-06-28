class TimeMap:

    def __init__(self):
        self.TimeMap = {}
        #intialize hashmap
   

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = {}
            #add key into hashmap
        if timestamp not in self.TimeMap[key]:
            self.TimeMap[key][timestamp] = []
            #add timestamp with key in hashamp
        self.TimeMap[key][timestamp].append(value)
        #now you've set the hashmap
        #key and timestamp go together, which gets you value
         

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap:
            return ""
            #no reason to look, it doesnt exist
        seen = 0

        for time in self.TimeMap[key]:
            #looping through timestamps
            if time <= timestamp:
                #track largest timestamp
                seen = max(seen, time)
        return "" if seen == 0 else self.TimeMap[key][seen][-1] 
        #now can return

        
