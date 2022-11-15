class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [999999 for i in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if(i+j >= len(nums)): break
                dp[i+j] = min(dp[i]+1,dp[i+j])
        return dp[len(nums)-1]

inp = [int(x) for x in input("Enter Input : ").split()]
sol = Solution()
print(sol.jump(inp))
