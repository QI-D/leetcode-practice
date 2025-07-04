'''
206. Reverse Linked List
Easy
Topics
conpanies icon
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        # A helper method for easy visualization
        nodes = []
        current = self
        while current:
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        iteratively_result = self.iteratively(head)
        return iteratively_result

        # recursive_result = self.recursively(head)
        # return recursive_result

    def iteratively(self, head):
        current = head
        prev = None

        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        return prev

    def recursively(self, head):
        if (not head) or (not head.next):
            return head
        
        prev = self.recursively(head.next)
        head.next.next = head
        head.next = None

        return prev


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

arr = [1,2,3,4,5]
head = create_linked_list(arr)
print(Solution().reverseList(head))

arr = [1,2]
head = create_linked_list(arr)
print(Solution().reverseList(head))
