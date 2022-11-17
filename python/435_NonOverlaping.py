class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ans=0
        sortedIn=sorted(intervals,key = lambda x:(x[1],x[0]))
        print(sortedIn)
        i=1
        while i < len(sortedIn):
            if sortedIn[i][0] < sortedIn[i-1][1] :
                sortedIn.pop(i)
                ans+=1
            else:
                i+=1
        return ans
intervals =[[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
sol = Solution()
print(sol.eraseOverlapIntervals(intervals))