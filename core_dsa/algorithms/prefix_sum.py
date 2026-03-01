# Subarray Sum Equals K
"""
Problem: Given an integer array nums and an integer k, 
find the number of subarrays whose sum equals k.  
"""
def subarray_sum_equals_k(nums: list[int], k: int) -> int :
    prefix_sum = 0 
    count = 0
    seen = {0:1} # {prefix_sum : frequency} , prefix_sum = 0 occured once

    for num in nums:
        prefix_sum = prefix_sum + num 

        if prefix_sum - k in seen:
            count = count + seen[prefix_sum - k]
        
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    
    return count

def main():
    nums = [1, 1, 1]
    k = 2
    print(subarray_sum_equals_k(nums, k))

if __name__ == "__main__":
    main()