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
