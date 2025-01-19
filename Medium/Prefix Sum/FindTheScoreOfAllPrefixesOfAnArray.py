def findPrefixScore(self, nums: List[int]) -> List[int]:
    maxPrefixArr = [] # List to store the maximum prefix sum.
    maxNum = 0

    # Calculate the maximum prefix sum.
    for i in range(len(nums)):
        if nums[i] > maxNum:
            maxNum = nums[i]

        maxPrefixArr.append(maxNum)

    res = []
    conver = []

    # Calculate the score of all prefixes.
    for i in range(len(nums)):
        conver.append(nums[i] + maxPrefixArr[i])
        if i == 0:
            res.append(conver[i])
        else:
            res.append(conver[i] + res[i - 1])
    return res

# Time Complexity: O(n), where n is the length of the input list nums.
# We iterate through the list twice to calculate the prefix sum.
# Space Complexity: O(n). We use two lists of size n to store the prefix sum and the maximum prefix array.