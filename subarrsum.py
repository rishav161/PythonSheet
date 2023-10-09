class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code he
       a=0
       sum=0
       for i in range(n):
           sum+=arr[i]
           if sum>=s:
               while(a<i and sum>s):
                   sum-=arr[a]
                   a=a+1
               if sum==s:
                   return [a+1,i+1]
       return [-1]
                   