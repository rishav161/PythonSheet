class Solution:
    def isBalanced(self,root):
    
        #add code here

        def Traverse(root):
            nonlocal flag
            if not root:
                return 0
            ls=Traverse(root.left)
            rs=Traverse(root.right)
            if abs(ls-rs)>1:
                flag=0
            return max(ls,rs)+1
        flag=1
        Traverse(root)
        return flag
