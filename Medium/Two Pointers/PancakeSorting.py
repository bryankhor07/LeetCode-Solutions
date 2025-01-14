def pancakeSort(self, nums: List[int]) -> List[int]:
    # Helper function to flip the elements of the list from index 0 to end
    def flip(end, nums):
        start = 0
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1

    N = len(nums)
    k_array = []
    # Iterate through the list from the end to the beginning
    # Find the maximum element in the unsorted part of the list
    # Flip the list to move the maximum element to the beginning
    for i in range(N-1,-1,-1):
        max = i
        for j in range(i,-1,-1):
            if nums[j] > nums[max]:
                max = j
        if max != i:
            flip(max, nums)
            flip(i, nums)
            k_array.append(max+1)
            k_array.append(i+1)
    return k_array

# Time Complexity: O(n^2), where n is the length of the input list nums. The outer loop runs n times, and in each iteration, the inner loop runs n times to find the maximum element. The flip operation takes O(n) time.
# Space Complexity: O(n). The space complexity is due to the list k_array, which stores the indices of the elements to be flipped. The maximum number of flips is 2n, so the space complexity is O(n).