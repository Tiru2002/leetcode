# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        self.traversal(root,l)
        return l
        
    def traversal(self,root,l):
        if root is None:
            return
        self.traversal(root.left,l)
        l.append(root.val)
        self.traversal(root.right,l)
