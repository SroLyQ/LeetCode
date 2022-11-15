class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=nums
        mx = dp[0]
        for i in range(0,len(nums)):
            if i-1 < 0 : continue
            if dp[i-1]<0 :
                dp[i] = dp[i]
            else:
                dp[i] = dp[i]+dp[i-1]
            mx = max(mx,dp[i])
        return mx
inp = [int(x) for x in input("Enter Input : ").split()]
sol = Solution()
print(sol.maxSubArray(inp))