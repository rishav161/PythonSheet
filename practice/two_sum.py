# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# nums = [2, 7, 11, 15]
 
# tar=16

def two_sum(arr,tar):
    num_map={}

    for i , num in enumerate(arr):
        comp=tar-num
        if comp in num_map:
            return [num_map[comp],i]
        
        num_map[num]=i
    return []
nums = [2, 7, 11, 15]
target = 13
print(two_sum(nums, target))
