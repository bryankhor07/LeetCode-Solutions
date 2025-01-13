def sortArrayByParity(self, nums: List[int]) -> List[int]:
    l = 0
    r = len(nums) - 1

    # Swap odd and even numbers using two pointers
    # l points to the leftmost odd number and r points to the rightmost even number in the list
    while l <= r:
        # Swap the numbers at l and r if l is odd and r is even
        if self.isOdd(nums[l]) and self.isEven(nums[r]):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1
        elif self.isOdd(nums[r]):
            r -= 1
        elif self.isEven(nums[l]):
            l += 1
    return nums


def isEven(self, n):
    return n % 2 == 0

def isOdd(self, n):
    return n % 2 != 0

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l, r, and the temporary variable temp.