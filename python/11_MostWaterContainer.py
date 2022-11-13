class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mx=0
        l,r=0,len(height)-1
        while (l<r):
            mx = max(mx,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return mx
            
inp = [int(i) for i in input().split()]
sol = Solution()
print(sol.maxArea(inp))