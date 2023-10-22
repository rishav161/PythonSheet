class Solution:
    def numberOfPaths (self, m, n):
        # print(a)
        pass
        # code here
        mod=10**9+7
        rs=1
        for i in range(m-1):
            rs=(rs*(m+n-2-i))%mod
            rs=rs*(pow(i+1,mod-2,mod))%mod

    return rs