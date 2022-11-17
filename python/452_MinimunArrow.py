class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sortPoint = sorted(points,key = lambda x:(x[0],-x[1]))
        minEnd = float('inf')
        ans=0
        for i in range(len(sortPoint)):
            if minEnd < sortPoint[i][0]:
                ans+=1
                minEnd = sortPoint[i][1]
            else:
                minEnd = min(minEnd,sortPoint[i][1])
        ans+=1

        return ans
points = [[4289383,51220269],[81692777,96329692],[57747793,81986128],[19885386,69645878],[96516649,186158070],[25202362,75692389],[83368690,85888749],[44897763,112411689],[65180540,105563966],[4089172,7544908]]
sol = Solution()
print(sol.findMinArrowShots(points))