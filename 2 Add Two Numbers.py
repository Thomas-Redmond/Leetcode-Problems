# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterate through array adding up nodes
        # Use a carry value

        cur = dummyHead = ListNode(0)       # init current node to dummy head of the returning list
        carry = 0                           # init carry to 0
        p = l1
        q = l2

        while p != None or q != None:       # Loop until both end
            if p != None: x = p.val         # set x to p.value unless if p ended in which case 0
            else: x = 0

            if q != None: y = q.val         # set y to q.value unless if q ended in which case 0
            else: y = 0

            sum = carry + x + y
            carry = sum // 10
            cur.next = ListNode(sum % 10)   # create new node with the digit value, and set to current nodes next
            cur = cur.next                      # advance current node to next

            if p != None: p = p.next        # advance both p and q
            if q != None: q = q.next

        if carry > 0:                       # if carry is left over at end of p and q
            cur.next = ListNode(carry)      # append new node with value 1

        return dummyHead.next               # return dummy head
