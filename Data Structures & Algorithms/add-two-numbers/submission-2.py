# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            #lists might not be the same size
            #handle the weird 8 + 7 case, don't forget to put or carry
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            #new digit/adding
            val = value1 + value2 + carry
            carry = val // 10 #case when > 10
            val = val % 10 #get the remainder that is val in that spot
            cur.next = ListNode(val)

            #update pointers
            cur = cur.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummy.next
        #dummy not a real node, points to actual node



        