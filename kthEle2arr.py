class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        arr1.extend(arr2)
        arr1=sorted(arr1)
        return arr1[k-1]
        