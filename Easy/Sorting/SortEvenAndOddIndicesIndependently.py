def sortEvenOdd(self, nums: List[int]) -> List[int]:
    if len(nums) <= 2:  # No sorting needed for 2 or fewer elements.
        return nums

    # Separate numbers by index parity.
    oddList = [nums[i] for i in range(1, len(nums), 2)]
    evenList = [nums[i] for i in range(0, len(nums), 2)]

    # Sort the lists.
    oddList.sort(reverse=True)
    evenList.sort()

    # Merge the sorted lists.
    res = []
    for i in range(max(len(evenList), len(oddList))):
        if i < len(evenList):
            res.append(evenList[i])
        if i < len(oddList):
            res.append(oddList[i])

    return res

# Time complexity: O(nlogn), where n is the length of the input list nums.
# The time complexity is dominated by the sorting operations on the even and odd lists.
# Space complexity: O(n), where n is the length of the input list nums.