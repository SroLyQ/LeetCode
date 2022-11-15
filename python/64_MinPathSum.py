class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j]=int(grid[i][j])
                if i==0 and j == 0:continue
                if i-1 < 0 : grid[i][j] += grid[i][j-1]
                elif j-1<0 : grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j]+= min(grid[i-1][j],grid[i][j-1])
        return grid[len(grid)-1][len(grid[len(grid)-1])-1]
mp = [x.split() for x in input("Enter row : ").split(',')]
sol = Solution()
print(sol.minPathSum(mp))        