class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(self.prefix_sum)):
            self.prefix_sum[i] = nums[i - 1] + self.prefix_sum[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.prefix_sum[right + 1] - self.prefix_sum[left]
        return self.prefix_sum[right + 1]
    
# Time Complexity: O(n), where n is the length of the input list nums.
# We iterate through the list once to calculate the prefix sum.
# Space Complexity: O(n). We use a list of size n to store the prefix sum.