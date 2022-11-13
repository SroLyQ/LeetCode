class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lmax=[]
        rmax=[]
        for i in range(len(height)):
            lmax.append(height[i])
            rmax.append(height[i])
        mx=0
        for i in range(len(lmax)):
            if i-1<0: continue
            lmax[i]=max(lmax[i],lmax[i-1])
        lmax.pop()
        for i in range(len(rmax),0,-1):
            if i+1>len(rmax)-1: continue
            rmax[i]=max(rmax[i],rmax[i+1])
        rmax.pop(0)
        real = [0 for i in range(len(rmax))]
        for i in range(len(real)):
            real[i] = min(rmax[i],lmax[i])
        start = 0
        end=0
        area = 0
        nextStart =0
        while(start <= end and start < len(real)):
            if(end >= len(real)):
                mx=max(mx,area)
                if(start == nextStart):
                    break
                area=0
                start=nextStart
                end=start
            if(real[start] == real[end]):
                area+=real[start]
                end+=1
            elif(real[start] < real[end]):
                area+=real[start]
                if(start == nextStart):
                    nextStart=end
                end+=1
            elif(real[start] > real[end]):
                area=0
                if(start == nextStart):
                    nextStart = end+1
                start=nextStart
                end=start
            mx = max(mx,area)
        start = len(real)-1
        end=start
        area = 0
        nextStart = start
        while(start >= end and start >= 0):
            if(end < 0):
                mx=max(mx,area)
                if(start == nextStart):
                    break
                area=0
                start=nextStart
                end=start
            if(real[start] == real[end]):
                area+=real[start]
                end-=1
            elif(real[start] < real[end]):
                area+=real[start]
                if(start == nextStart):
                    nextStart=end
                end-=1
            elif(real[start] > real[end]):
                area=0
                if(start == nextStart):
                    nextStart = end-1
                start=nextStart
                end=start
            mx = max(mx,area)
        return mx
            
inp = [int(i) for i in input().split()]
sol = Solution()
print(sol.maxArea(inp))