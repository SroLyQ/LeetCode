class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        dic_s = dict()
        for char in s:
           if char in target:
                if char not in dic_s.keys():
                    dic_s[char]=1
                else:
                    dic_s[char]+=1
        dic_c = dict()
        for char in target:
            if char not in dic_c.keys():
                dic_c[char]=1
            else:
                dic_c[char]+=1
        ans=[]
        if(len(dic_s.keys()) < len(dic_c.keys())):
            return 0
        for char in target:
            if char in dic_s.keys() and char in dic_c.keys():
                ans.append(dic_s[char]//dic_c[char])
        return min(i for i in ans)
s = input()
target = input()
sol = Solution()
print(sol.rearrangeCharacters(s,target))