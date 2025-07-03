'''
328. Odd Even Linked List
Medium
Topics
conpanies icon
Companies
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
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
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even # the start of the even indexed list

        while even and even.next:
            odd.next = odd.next.next # skip even node, link to next odd node
            even.next = even.next.next # skip next odd node, link to next even node

            odd = odd.next
            even = even.next

        odd.next = even_head # reconnect odd and even

        return head

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
print(Solution().oddEvenList(head)) # expect [1,3,5,2,4]

arr = [2,1,3,5,6,4,7]
head = create_linked_list(arr)
print(Solution().oddEvenList(head)) # expect [2,3,6,7,1,5,4]
