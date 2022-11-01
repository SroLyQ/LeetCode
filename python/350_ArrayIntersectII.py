class Solution(object):
    def intersect(self,nums1,nums2):
        ans1=[]
        for i in nums1:
            if i in nums2:
                ans1.append(i)
                nums2.remove(i)
        return ans1
inp =[int(x) for x in input("Enter Input : ").split()]
inp2 = [int(y) for y in input("Enter 2 Input : ").split()]
sol = Solution()
print(sol.intersect(inp,inp2))

