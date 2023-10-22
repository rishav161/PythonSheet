  def maxSubArraySum(self,arr,N):
        ##Your code here
        currsum=0
        maxsum=-1e8
        for i in range(0,N):
            currsum+=arr[i]
            if currsum>maxsum:
                maxsum=currsum
            if currsum<0:
                currsum=0
        return maxsum