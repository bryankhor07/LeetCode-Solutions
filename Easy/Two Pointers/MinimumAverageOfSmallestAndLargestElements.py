def minimumAverage(self, nums: List[int]) -> float:
    nums.sort()
    averages = []
    l, r = 0, len(nums) - 1

    # Calculate the average of the smallest and largest elements
    while l < r:
        averages.append((nums[l] + nums[r]) / 2)
        l += 1
        r -= 1
    
    averages.sort()
    return averages[0]

# Time Complexity: O(n log n), where n is the length of the input list nums. The time complexity is due to the sorting of the input list.
# Space Complexity: O(n). The space complexity is due to the list averages, which stores the average of the smallest and largest elements of the input list.