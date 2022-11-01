class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if(nums[i]+nums[j]+nums[k] == 0 and i!=j and j!=k and i!=k):
                        a = [nums[i],nums[j],nums[k]]
                        a.sort()
                        ans.add(tuple(a))
        return list(ans)


inp = [int(x) for x in input().split()]
sol = Solution()
ans = Solution.threeSum(sol,inp)
print(ans)