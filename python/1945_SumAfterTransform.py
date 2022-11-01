class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = ''
        for char in s:
            ans+=str(ord(char)-ord('a')+1)
        while(k):
            tempans = 0
            for digit in ans:
                tempans+=int(digit)
            ans = str(tempans)
            k-=1
        return int(ans)

inp = input()
k = int(input())

sol = Solution()
ans=sol.getLucky(inp,k)
print(ans)