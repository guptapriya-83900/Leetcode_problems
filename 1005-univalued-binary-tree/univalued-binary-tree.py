# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def check(p,value):
            if not p:
                return True

            if p.val!=value:
                return False

            return check(p.left,value) and check(p.right,value)

        if check(root.left, root.val) and check(root.right, root.val):
            return True
        else:
            return False
            
        


        
