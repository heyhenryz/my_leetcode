# if asked to return list of TreeNodes
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1, n)
    
    def helper(self, min_, max_):
        result = []
        if min_ > max_:
            return result
        for num in range(min_, max_+1):
            leftlist = self.helper(min_, num-1)
            rightlist = self.helper(num+1, max_)
            if len(leftlist) == 0 and len(rightlist) == 0:
                root = TreeNode(num)
                result.append(root)
            elif len(leftlist) == 0:
                for right in rightlist:
                    root = TreeNode(num)
                    root.right = right
                    result.append(root)
            elif len(rightlist) == 0:
                for left in leftlist:
                    root = TreeNode(num)
                    root.left = left
                    result.append(root)
            else:
                for left in leftlist:
                    for right in rightlist:
                        root = TreeNode(num)
                        root.left = left
                        root.right = right
                        result.append(root)
        return result

    
    
#
if the return needs to be a list of list of number

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        node_result = self.helper(1, n)
        result = []
        for root in node_result:
            result.append(self.node_to_list(root))
        return result
        
    def node_to_list(self, root):
        from collections import deque
        res = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(node.val)                               
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append(None)
        while res and not res[-1]:
            res.pop()
        return res
    
    def helper(self, min_, max_):
        result = []
        if min_ > max_:
            return result
        for num in range(min_, max_+1):
            leftlist = self.helper(min_, num-1)
            rightlist = self.helper(num+1, max_)
            if len(leftlist) == 0 and len(rightlist) == 0:
                root = TreeNode(num)
                result.append(root)
            elif len(leftlist) == 0:
                for right in rightlist:
                    root = TreeNode(num)
                    root.right = right
                    result.append(root)
            elif len(rightlist) == 0:
                for left in leftlist:
                    root = TreeNode(num)
                    root.left = left
                    result.append(root)
            else:
                for left in leftlist:
                    for right in rightlist:
                        root = TreeNode(num)
                        root.left = left
                        root.right = right
                        result.append(root)
        return result 
