# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        c=1
        n=head
        while n.next:
            c+=1
            n=n.next
        k%=c           
        if k==0:       
            return head

        n.next=head
        n=head
        c-=k
        while c>1:
            c-=1
            n=n.next
            
        p=n.next
        n.next=None
        return p


        
        