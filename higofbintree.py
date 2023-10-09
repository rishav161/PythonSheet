def height(self, root):
        # code here
        if root == None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left , right)