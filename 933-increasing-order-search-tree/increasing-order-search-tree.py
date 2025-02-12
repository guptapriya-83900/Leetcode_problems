# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy=TreeNode(0)
        self.curr=dummy
        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            node.left=None
            self.curr.right=node
            self.curr=self.curr.right

            inorder(node.right)

        inorder(root)
        return dummy.right




        