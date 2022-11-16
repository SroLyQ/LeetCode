class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(nums))]
        dp[0]= nums[0]
        if(len(nums)>1):
            dp[1]=nums[1]
        for i in range(len(nums)):
            if i-2 >=0 : dp[i]=max(nums[i]+dp[i-2],dp[i])
            if i-3>=0 : dp[i] = max(nums[i]+dp[i-3],dp[i])
        return max(dp[len(nums)-1],dp[len(nums)-2])
nums = [2,7,3,9,1]
sol=Solution()
print(sol.rob(nums))