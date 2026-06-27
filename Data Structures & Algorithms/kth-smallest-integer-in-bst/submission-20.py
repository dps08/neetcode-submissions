# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.num = 0
        def inorder(node):
            if not node:
                return
            
            left1 = inorder(node.left)
            if left1 is not None:
                    return left1
            self.num += 1
            if self.num == k:
                return node.val
            return inorder(node.right)
            
        output = inorder(root)
        return output