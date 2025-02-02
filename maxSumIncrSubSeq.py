def maxSumIS(self, arr, n):
		# code here
	li=[]
	maxsum=0
	for i in range(n):
		li.append(arr[i])
    for i in range(n):
        for j in range(0,i):
            if arr[i]>arr[j]:
                li[i]=max(li[i],li[j]+arr[i])
        maxsum=max(li[i],maxsum)
    return maxsum
maxSumIS([1,2,3,4,5],3)