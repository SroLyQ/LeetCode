class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sortPoint = sorted(points,key = lambda x:(x[0],-x[1]))
        for i in range(len(sortPoint))
        return sortPoint
points = [[10,16],[2,8],[1,6],[7,12]]
sol = Solution()
print(sol.findMinArrowShots(points))