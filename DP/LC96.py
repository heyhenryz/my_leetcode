#96. Unique Binary Search Trees

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # we use dynamic programming to solve this problem
        # when n = 1: we have only 1 BSt
        # n = 2, we have 2 bst,
        #  1               2
        #    \            /
        #     2          1
        # n = 3, 5 bst = 1 * 2 + 1 + 2 * 1 = 5
        #     1                      2            3
        #      \                    /\           /
        #      (2 nodes)           1  3       (2 nodes)
        #
        #n = 4,  =  1*5 + 1*2 + 2*1 + 5*1
        #   1                2                 3                4
        #     \              /\                /  \           /
        #      (3 nodes)    1  (2nodes)    (2 nodes) 4        (3 nodes)
        # so the induction principle is:
        # dp[n] = sum(j from 0 to n-1) dp[j] * dp [n-1-j]
        
        if n < 0:
            return None
        if n <= 1:
            return 1
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
