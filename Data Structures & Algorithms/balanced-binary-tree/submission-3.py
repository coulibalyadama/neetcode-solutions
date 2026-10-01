# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # self.res = True

        # def dfs(node):
        #     if not node:
        #         return 0

        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     if max(left, right) - min(left, right) > 1:
        #         self.res = False

        #     return 1 + max(dfs(node.left), dfs(node.right))

        # dfs(root)
        
        # return self.res

        def dfs(node):
            if not node: return [True, 0]

            left, right = dfs(node.left), dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1])<=1

            return [balanced, 1+max(left[1], right[1])]

        return dfs(root)[0]
        