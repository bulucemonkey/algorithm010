# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        result = l3
        while True:
            if l1 == l2:
                result = l1
                break
            elif l2 == None:
                result = l1
                break
            elif l1 == None:
                result = l2
                break
            elif l1.val < l2.val:
                l3.val = l1.val
                l1 = l1.next
                if l1 == None:
                    l3.next = l2
                    break
                l3.next = ListNode(0)
                l3 = l3.next
            else:
                l3.val = l2.val
                l2 = l2.next
                if l2 == None:
                    l3.next = l1
                    break
                l3.next = ListNode(0)
                l3 = l3.next

        return result
