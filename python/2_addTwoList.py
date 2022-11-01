class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1;
        cur2 = l2;
        head1 = cur1;
        head2 = cur2;
        tod = (cur1.val+cur2.val)//10
        ans = ListNode((cur1.val+cur2.val)%10)
        head = ans
        cur1=cur1.next
        cur2=cur2.next
        while(cur1 and cur2):
            ans.next = ListNode((cur1.val+cur2.val+tod)%10)
            tod = (cur1.val + cur2.val + tod)//10
            cur1=cur1.next
            cur2=cur2.next
            ans = ans.next
        while(cur1):
            ans.next = ListNode((cur1.val+tod)%10)
            tod = (cur1.val+tod)//10
            ans=ans.next
            cur1=cur1.next
        while(cur2):
            ans.next = ListNode((cur2.val+tod)%10)
            tod = (cur2.val+tod)//10
            ans=ans.next
            cur2=cur2.next
        if(tod > 0):
            ans.next = ListNode(tod)
        return head

l1 = [int(x) for x in input().split()]
l2 = [int(y) for y in input().split()]
print(l1,l2)

headl1 = ListNode(l1[0])
cur1 = headl1
for i in range(1,len(l1)):
    cur1.next = ListNode(l1[i]);
    cur1 = cur1.next
headl2 = ListNode(l2[0])
cur2 = headl2
for i in range(1,len(l2)):
    cur2.next = ListNode(l2[i]);
    cur2 = cur2.next
sol = Solution()
ans = Solution.addTwoNumbers(sol,headl1,headl2)
while (ans):
    print(ans.val,end=" ")
    ans=ans.next