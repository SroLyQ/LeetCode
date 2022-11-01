class Solution(object):
    def intersection(self,nums1,nums2):
        n1=set(nums1)
        n2=set(nums2)
        ans = n1&n2
        return list(ans)

inp =[int(x) for x in input("Enter Input : ").split()]
inp2 = [int(y) for y in input("Enter 2 Input : ").split()]
sol = Solution()
print(sol.intersection(inp,inp2))

