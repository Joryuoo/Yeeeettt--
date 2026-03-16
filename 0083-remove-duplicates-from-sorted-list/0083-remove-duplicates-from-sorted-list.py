# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        seen = []

        curr = head
        prev = head
        while curr:
            if curr.val in seen:
                prev.next = curr.next
            else:
                seen.append(curr.val)
                prev = curr
            curr = curr.next
        return head
                
        