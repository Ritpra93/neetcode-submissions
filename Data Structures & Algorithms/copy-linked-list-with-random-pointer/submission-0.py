"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
         hash_for_copying = {None : None}
         cur = head
         while cur:
            copy = Node(cur.val)
            hash_for_copying[cur] = copy
            #map current to it's value in hashmap, making deep copy
            cur = cur.next
         cur = head
            #reset after passing through
         while cur:
                copy = hash_for_copying[cur]
                #gets the current value
                copy.next = hash_for_copying[cur.next]
                copy.random = hash_for_copying[cur.random]
                #now get the random value from cur
                cur = cur.next
         return hash_for_copying[head]




        