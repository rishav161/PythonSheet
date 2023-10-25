class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x=temp=ListNode(0)
        cur=temp.next=head
        while cur and cur.next:
            val=cur.next.val
            if cur.val<val:
                cur=cur.next
                continue
            if x.next.val>val:
                x=temp
            while x.next.val<val:
                x=x.next
            new=cur.next
            cur.next=new.next
            new.next=x.next
            x.next=new
        return temp.next