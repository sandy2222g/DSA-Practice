class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n=0
        fast=head
        slow=head
        if not head:
            return 0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            n+=2
        p=None
        while slow:
            nxt=slow.next
            slow.next=p
            p=slow
            slow=nxt
        m=0
        while p:
            m=max(m,p.val+head.val)
            head=head.next
            p=p.next
        return m
