'''
110. Balanced Binary Tree
Easy
Topics
Companies
Given a binary tree, determine if it is 
height-balanced
.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        from collections import deque
        queue = deque([self])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        # Remove trailing nulls for a cleaner output
        while result and result[-1] == "null":
            result.pop()
        
        print("[" + ", ".join(result) + "]")

class Solution:
    def isBalanced(self, root):
        def checkHeight(node):
            if not node:
                return 0
            
            left_height = checkHeight(node.left)
            if left_height == -1:
                return -1
            
            right_height = checkHeight(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return checkHeight(root) != -1

# Tree 1: [3, 9, 20, null, null, 15, 7]
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

# Tree 2: [1, 2, 2, 3, 3, null, null, 4, 4]
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)

# Tree 3: []
root3 = None

solution = Solution()

print("Tree 1:")
root1.printTree()
print("Is Balanced:", solution.isBalanced(root1))

print("\nTree 2:")
root2.printTree()
print("Is Balanced:", solution.isBalanced(root2))

print("\nTree 3:")
if root3:
    root3.printTree()
else:
    print("[]")
print("Is Balanced:", solution.isBalanced(root3))
