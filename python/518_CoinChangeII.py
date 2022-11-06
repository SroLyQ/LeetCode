class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for i in range(amount+1)]
        coins = sorted(coins)
        dp[0]=1
        for coin in coins:
            for i in range(amount+1):
                if(i-coin<0): continue
                dp[i]+=dp[i-coin]
        return dp[amount]
inp,val = input().split(',')
inp = [int(x) for x in inp.split()]
sol =Solution()
print(sol.change(int(val),inp))