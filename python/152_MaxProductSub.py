class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = max(nums)
        nowMax,nowMin=1,1
        for i in nums:
            if i == 0 : nowMax,nowMin=1,1
            tmp = nowMax
            nowMax = max(i,nowMax*i,nowMin*i)
            nowMin = min(i,tmp*i,nowMin*i)
            ans = max(ans,nowMax)
        return ans

nums = [-2]
sol = Solution()
print(sol.maxProduct(nums))