def rearrangeArray(self, nums: List[int]) -> List[int]:
    positiveNums = []
    negativeNums = []
    res = []

    # Separate positive and negative numbers
    for num in nums:
        if num > 0:
            positiveNums.append(num)
        else:
            negativeNums.append(num)

    # Rearrange the numbers by alternating between positive and negative numbers
    for i in range(len(positiveNums)):
        res.append(positiveNums[i])
        res.append(negativeNums[i])
    return res

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(n). The space complexity is due to the two lists positiveNums and negativeNums, which store the positive and negative numbers, respectively. The total space used by these lists is O(n).