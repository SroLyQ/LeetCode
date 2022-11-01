class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title=title.split()
        ans=''
        for i in range(len(title)):
            if len(title[i])>2:
                tempWord=title[i].capitalize()
            else:
                tempWord=title[i].lower()
            if(i!=len(title)-1):
                ans+=tempWord
                ans+=' '
            else:
                ans+=tempWord
        return ans
inp = input()
sol =Solution()
print(sol.capitalizeTitle(inp))