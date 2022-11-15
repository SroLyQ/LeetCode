class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if j==0 and i == 0: continue
                if j-1 < 0: dp[i][j] = dp[i-1][j]
                elif i-1 < 0 : dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]
m,n = input("Enter Input : ").split()
m,n = int(m),int(n)
sol = Solution()
print(sol.uniquePaths(m,n))