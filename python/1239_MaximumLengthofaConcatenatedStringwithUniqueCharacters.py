class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        uniqWord = []

        for word in arr:
            if len(set(word))==len(word):
                uniqWord.append(word)
        
        mySet = ['']

        for i in range(len(uniqWord)):
           for tset in mySet:
            if len(set(tset+uniqWord[i])) == len(tset+uniqWord[i]):
                mySet.append(tset + uniqWord[i])

        mx=0
        for word in mySet:
            mx=max(mx,len(str(word)))
        
        return mx
                    
word = input().split()
sol = Solution()
ans=sol.maxLength(word)
print(ans)