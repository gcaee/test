# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Raspberry Pi

class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        sort = list()
        empty = ListNode("")

        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                sort.append(l1.val)
                l1 = l1.next
            else:
                sort.append(l2.val)
                l2 = l2.next

        while l1 != None:
            sort.append(l1.val)
            l1 = l1.next
        while l2 != None:
            sort.append(l2.val)
            l2 = l2.next

        return sort
