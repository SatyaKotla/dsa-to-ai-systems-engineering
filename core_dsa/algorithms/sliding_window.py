# Longest substring without repeating characters
"""
Problem: Given a string s, return the length of the 
longest substring without duplicate characters. 

Approach: Sliding Window with Hash Set
"""
def length_of_longest_substring(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    left = 0 
    right = 0
    n = 0
    seen = set()
    
    while right < len(s):
        if s[right] not in seen:
            seen.add(s[right])
            n = max(n, right-left + 1)
            right = right + 1
        else:
            seen.remove(s[left])
            left = left + 1
    return n 

# Maximum Sum Subarray of Size K
"""
Problem: Given an array of integers and an integer k, 
return the maximum sum of any contiguous subarray of size k. 
"""
def max_sum_subarray(nums: list[int], k: int) -> int:

    if k > len(nums):
        raise ValueError("k cannot be greater than the length of the list.")
    
    # first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    #progression
    left = 1
    right = k 
    
    while right < len(nums):
        window_sum = window_sum + nums[right] - nums[left - 1]
        max_sum = max(window_sum, max_sum)
        right = right + 1
        left = left + 1 
    return max_sum

# Longest Substring With At Most K Distinct Characters
"""
Problem: Given a string s and integer k, return the 
length of the longest substring that contains at most
k distinct characters.
"""
def longest_substring_k_distinct(s: str, k: int) -> int:
    left = 0 
    max_len = 0 
    freq = {}

    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1 

        while len(freq) > k:
            left_char = s[left]
            freq[left_char] = freq[left_char] - 1 
            if freq[left_char] == 0:
                del freq[left_char]
            left = left + 1
        max_len = max(max_len, right - left + 1)
    
    return max_len
        

def main():
   s = "abcdc"
   k =2
   print(longest_substring_k_distinct(s, k))

if __name__ == "__main__":
    main()
