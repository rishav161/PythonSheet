class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        kp=[0]*(W+1)
        for i in range(1,W+1):
            for j in range(N):
                if wt[j]<=i:
                    kp[i]=max(kp[i],kp[i-wt[j]]+val[j])
        return kp[W]