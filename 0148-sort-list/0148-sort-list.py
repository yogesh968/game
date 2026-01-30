class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 or l2
        return dummy.next
