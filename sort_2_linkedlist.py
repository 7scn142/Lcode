class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next: return head
        
        fast = head.next; slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        fast = slow.next
        slow.next = None
        l0 = self.sortList(head)
        l1 = self.sortList(fast)
        
        return self.merge(l0, l1)
    
    def merge(self, head0, head1):
        run0 = head0; run1 = head1
        dummyHead = ListNode(-1); run = dummyHead
        
        while run0 and run1:
            if run0.val < run1.val:
                run.next = run0
                run0 = run0.next
            else:
                run.next = run1
                run1 = run1.next
            run = run.next
            
        if not run0: run.next = run1
        if not run1: run.next = run0
            
        return dummyHead.next
