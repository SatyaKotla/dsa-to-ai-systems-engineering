"""
Kadane and Optimzation Problems:
- Maximum subarray
- Maximum product subarray
- Maximum sum rectangle (2D Kadane)

"""

# Kadane's algorithm
"""
Problem: Given an integer array nums, return the maximum
sum of any contiguous array. 
"""
def subarray_sum_max(nums: list[int]) -> int:
    if not nums:
        return 0 
    # variable intiation at index 0
    current_sum = nums[0]
    maximum_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        maximum_sum = max(maximum_sum, current_sum)
    
    return maximum_sum

# Maximum Product Subarray
"""
Problem: Given an integer array nums, return the maximum product
of a contiguous subarray. 
"""
def subarray_product_max(nums: list[int]) -> int:
    if not nums:
        return 0 
    maximum_product = nums[0]
    minimum_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        temp_max = maximum_product
        maximum_product = max(nums[i],
                              nums[i]*temp_max,
                              nums[i]*minimum_product)
        minimum_product = min(nums[i],
                              nums[i]*temp_max,
                              nums[i]*minimum_product)
        result = max(result, maximum_product)
    
    return result

# 2D Kadane's Algorithm
"""
Problem: Given a 2D matrix, find the sub-rectangle with 
maximum sum
"""
def sub_rectangle_sum_max(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0 
    
    rows = len(matrix)
    columns = len(matrix[0])

    maximum_sum = float("-inf")

    # Fix the left column 
    for left in range(columns):
        temp = [0]*rows

        # expand the right column:
        for right in range(left, columns):

            # compress rows
            for r in range(rows):
                temp[r] += matrix[r][right]
            
            # apply 1D Kadane's algorithm on the temp 
            current_sum = temp[0]
            best_sum = temp[0]

            for i in range(1, rows):
                current_sum = max(temp[i], current_sum + temp[i])
                best_sum = max(best_sum, current_sum)
            
            maximum_sum = max(maximum_sum, best_sum)
    
    return maximum_sum

def main():
    matrix = [
        [1, 2, -1, -2, -20],
        [-8, -3, 4, 3, 1],
        [3, 4, 11, 12, 3],
        [-4, -1, 2, 3, -9]
    ]
    print(sub_rectangle_sum_max((matrix)))

if __name__ == "__main__":
    main()