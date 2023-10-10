class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        # Your Code Here

        A.sort()
        for i in range(0,(n-2)):
            l=i+1
            r=n-1
            while l<r:
                if A[i]+A[l]+A[r]==X:
                    return True
                elif A[l]+A[r]<X-A[i]:
                    l+=1
                elif A[l]+A[r]>X-A[i]:
                    r=r-1
        return False