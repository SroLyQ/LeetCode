class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans=0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j]=int(matrix[i][j])
                if(matrix[i][j]==1 and i>0 and j >0):
                    matrix[i][j] = matrix[i][j]+min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1]) 
                ans=max(matrix[i][j],ans)
        return ans**2
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
sol = Solution()
print(sol.maximalSquare(matrix))