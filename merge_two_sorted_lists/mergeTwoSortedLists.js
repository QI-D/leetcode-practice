/**
 * 21. Merge Two Sorted Lists
Solved
Easy
Topics
conpanies icon
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

// ListNode constructor
function ListNode(val, next = null) {
  this.val = val;
  this.next = next;
}

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let dummy = new ListNode();
    let current = dummy;

    while (list1 && list2) {
        if (list1.val < list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }

    if (list1) {
        current.next = list1
    }
    if (list2) {
        current.next = list2
    }

    return dummy.next;
};

// Helper: Convert array to linked list
function arrayToList(arr) {
  let dummy = new ListNode();
  let current = dummy;
  for (let val of arr) {
    current.next = new ListNode(val);
    current = current.next;
  }
  return dummy.next;
}

// Helper: Convert linked list to array (for easy display)
function listToArray(list) {
  const result = [];
  while (list) {
    result.push(list.val);
    list = list.next;
  }
  return result;
}

// Test case
const list1 = arrayToList([1, 2, 4]);
const list2 = arrayToList([1, 3, 4]);
const merged = mergeTwoLists(list1, list2);

console.log("Merged list:", listToArray(merged)); // Output: [1, 1, 2, 3, 4, 4]
