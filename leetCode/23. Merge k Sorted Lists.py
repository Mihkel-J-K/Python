# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        solution = []
        for i in lists:
            solution += i.val
            x = i.next
            while x != None:
                solution += x.val
                x = x.next
        return solution

