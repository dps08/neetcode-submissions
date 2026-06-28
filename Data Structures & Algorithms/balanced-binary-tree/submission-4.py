# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            d = abs(left_height - right_height)

            if d > 1:
                return -1

            if left_height == -1:
                return -1

            if right_height == -1:
                return -1 

            height_of_node = 1 + max(left_height, right_height)

            return height_of_node

        return height(root) != -1

        
        