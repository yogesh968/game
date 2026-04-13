# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        champa = ListNode(0)
        dummy = champa 

        count = []
        while temp:
            count.append(temp.val)
            temp = temp.next 
        
        count = count[::-1]
        
        for i in range(len(count)):
            dummy.next = ListNode(count[i])
            dummy  = dummy.next

          
        return champa.next
