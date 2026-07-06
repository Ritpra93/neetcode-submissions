class LRUCache:
    #ideas can this be a hashmap with a size
    #can use ordered dict for this 


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU_Cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.LRU_Cache:
            return -1
        self.LRU_Cache.move_to_end(key)
        return self.LRU_Cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.LRU_Cache:
            self.LRU_Cache.move_to_end(key)
        self.LRU_Cache[key] = value
        if len(self.LRU_Cache) > self.capacity:
            #linked list implementation or can do this?
            self.LRU_Cache.popitem(last=False)



        
