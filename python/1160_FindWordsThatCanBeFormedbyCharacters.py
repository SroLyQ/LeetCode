class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chardic = dict()
        ans = 0
        for i in chars:
            if i in chardic.keys():
                chardic[i] += 1
            else:
                chardic[i] = 1
        for word in words:
            dictcp = chardic.copy()
            canCreate = True
            for char in word:
                if not char in dictcp.keys():
                    canCreate=False
                    break
                if dictcp[char] > 0:
                    dictcp[char]-=1
                else:
                    canCreate=False
                    break
            if canCreate:
                ans+=len(word)

        return ans
word = input().split()
char = input()
sol = Solution()
ans=sol.countCharacters(word,char)
print(ans)