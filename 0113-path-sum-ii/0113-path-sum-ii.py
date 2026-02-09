class Solution:
    def pathSum(self, root, targetSum):
        res = []
        
        def dfs(node, curr, total):
            if not node:
                return
            curr.append(node.val)
            total += node.val
            if not node.left and not node.right and total == targetSum:
                res.append(curr[:])
            dfs(node.left, curr, total)
            dfs(node.right, curr, total)
            curr.pop()
        
        dfs(root, [], 0)
        return res
