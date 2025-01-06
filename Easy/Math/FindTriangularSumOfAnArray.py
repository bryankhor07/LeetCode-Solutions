def triangularSum(self, nums: List[int]) -> int:
    # Get the length of the input list
    n = len(nums)
    
    # Repeat the process n-1 times to reduce the list to a single number
    for _ in range(n - 1):
        # Create a new list to store the result of the current iteration
        newNums = []
        
        # Iterate through the list, summing adjacent elements and taking the modulo 10
        for i in range(len(nums) - 1):
            # Append the result of the sum to the newNums list
            newNums.append((nums[i] + nums[i + 1]) % 10)
        
        # Update nums to the newNums list for the next iteration
        nums = newNums
    
    # Return the last remaining number in the list
    return nums[0]

# Time Complexity: O(n^2)
# Space Complexity: O(n)