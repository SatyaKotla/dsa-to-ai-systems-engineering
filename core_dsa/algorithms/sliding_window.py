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

def main():
    s = input(f"Please provide your string input: ")
    print(length_of_longest_substring(s))

if __name__ == "__main__":
    main()

