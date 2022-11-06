class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lmax = height.copy()
        rmax = height.copy()

        for i in range(len(lmax)):
            if i-1<0: continue
            lmax[i]=max(lmax[i],lmax[i-1])
        for i in range(len(rmax),0,-1):
            if i+1>len(rmax)-1: continue
            rmax[i]=max(rmax[i],rmax[i+1])
        
        print(lmax,rmax)
inp = [int(i) for i in input().split()]
sol = Solution()
print(sol.maxArea(inp))