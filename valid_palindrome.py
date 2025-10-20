# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        tracking_stack = []
        curr_pointer = head
        while curr_pointer is not None:
            tracking_stack.append(curr_pointer.val)
            curr_pointer = curr_pointer.next

        while head is not None:
            character_to_check = tracking_stack.pop()
            if (head.val != character_to_check):
                return False
            head = head.next

        return True
