def numberOfPoints(self, nums: List[List[int]]) -> int:
    # Find the maximum range value to limit our array size
    max_point = max([end for _, end in nums])
    
    # Initialize a difference array
    diff = [0] * (max_point + 2)
    
    # Mark the start and end of each interval
    for start, end in nums:
        diff[start] += 1
        diff[end + 1] -= 1
    
    # Compute the prefix sum to get the count of covered points
    count = 0
    curr_sum = 0
    for value in diff:
        curr_sum += value
        if curr_sum > 0:  # A point is covered if the current sum is > 0
            count += 1
    
    return count

# Time Complexity: O(n), where n is the length of the input list nums.
# We iterate through the list once to calculate the prefix sum.
# Space Complexity: O(n). We use a list of size n to store the prefix sum.