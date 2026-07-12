# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #make a copy 
        #reverse the copy the same way you'd reverse a linked list
        #left and right pointers so you only reverse that portion?
        dummy_node = ListNode(0, head)
        #create a dummy node 
        groupPrevNode = dummy_node


        while True:
            kth_node = self.getKth(groupPrevNode, k)
            #helper function to find kth node
            if not kth_node:
                break
            groupNextNode = kth_node.next
            prev, curr = kth_node.next, groupPrevNode.next
            #the normal way you'd reverse, for the current grpup 
            while curr != groupNextNode:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrevNode.next
            groupPrevNode.next = kth_node
            groupPrevNode = temp
        return dummy_node.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -=1
        return curr

  
