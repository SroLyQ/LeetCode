class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        mp=[[1 for j in range(len(obstacleGrid[0]))]for i in range(len(obstacleGrid))]
        for i in range(len(mp)):
            for j in range(len(mp[i])):
                if obstacleGrid[i][j] == 1 : 
                    mp[i][j]=0
                    continue
                if i == 0 and j==0 : continue
                if j-1 < 0: mp[i][j] = mp[i-1][j]
                elif i-1 < 0 : mp[i][j] = mp[i][j-1]
                else:
                    mp[i][j] = mp[i][j-1]+mp[i-1][j]
        return mp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
        
mp = [x.split() for x in input("Enter row : ").split(',')]
sol = Solution()
print(sol.uniquePathsWithObstacles(mp))