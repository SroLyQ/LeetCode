class Solution(object):
    def longestPalindrome(self, s):
        ans = ''
        for i in range(len(s)):
            start = i
            cnt = 0
            j=len(s)-1
            end = len(s)-1
            newTry = True
            ansEnd = 0
            while(start < end):
                if(s[start] == s[end]):
                    if(newTry):
                        ansEnd = end
                        newTry =False
                    start +=1
                    end -=1
                elif(s[start]!=s[end]):
                    newTry = True
                    cnt+=1
                    start = i
                    end = j-cnt
                    ansEnd=i
            ansS = s[i:ansEnd+1]
            if len(ansS) > len(ans):
                ans = ansS
        return ans
            

inp = input("Enter Input : ")
sol = Solution()
ans = sol.longestPalindrome(inp)
print(ans)
        