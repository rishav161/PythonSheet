	def minSwaps(self, nums):
		#Code here
		n=len(nums)
		li=[]
		for i in range(n):
		    li.append([nums[i],i])
		li.sort()
		visited=[False for i in range(n)]
		ans=0
		for i in range(n):
		    if visited[i] or li[i][1]==i:
		        continue
		    else:
		        size=0
		        j=i
		        while(visited[j]==False):
		            visited[j]=True
		            j=li[j][1]
		            size=size+1
		        ans=ans+max(0,size-1)
		return ans