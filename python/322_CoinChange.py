class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        dp=[999999999 for i in range(amount+1)]
        dp[0]=0
        for i in range(amount+1):
            for coin in coins:
                if(i-coin < 0): continue
                if(dp[i-coin]+1 < dp[i]): dp[i]=dp[i-coin]+1
        if dp[amount] == 999999999:
            return -1
        else:
            return dp[amount]
inp,val = input().split(',')
inp = [int(x) for x in inp.split()]
sol =Solution()
print(sol.coinChange(inp,int(val)))
