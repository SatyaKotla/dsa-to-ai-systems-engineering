"""
Prefix Sum Based Problems:
- Counting subarrays
- Divisibility conditions
- Frequency map usage
"""

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

# Continous Subarray Sum
"""
Problem: Given a list nums and and integer k, return True if there
exists a subarray of size >= 2 whose sum is a multiple of k. 
"""
def subarray_sum_multiples_of_k(nums: list[int], k: int) -> bool:
    prefix_sum = 0 
    seen = {0:-1} # remainder: first index where it appeared

    for i, num in enumerate(nums):
        prefix_sum = prefix_sum + num 
        remainder = prefix_sum % k if k!=0 else prefix_sum # to avoid zero division

        if remainder in seen:
            if i - seen[remainder] > 1:
                return True 
        else:
            seen[remainder] = i 
    return False

def main():
    nums = [2, 1, 3, 6]
    k = 4
    print(subarray_sum_multiples_of_k(nums, k))

if __name__ == "__main__":
    main()