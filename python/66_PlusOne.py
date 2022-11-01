from string import digits
from unicodedata import digit


class Solution(object):
    def plusOne(self, digits):
        digits.reverse()
        num=(digits[0]+1)%10
        tod = (digits[0] + 1)//10
        digits[0]=num
        for i in range(1,len(digits)):
            num = (digits[i]+tod)%10
            tod = (digits[i]+tod)//10
            digits[i]=num
        if tod > 0:
            digits.append(tod)
        digits.reverse()
        return digits
inp = [int(x) for x in input().split()]
sol = Solution()
ans=sol.plusOne(inp)
print(ans)