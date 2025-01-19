def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Summary: This function returns an array res such that each element 
    #          at index i of res is the product of all the numbers in the input 
    #          array nums except nums[i]. It achieves this without using division and 
    #          in O(n) time by using two passes through the list to accumulate prefix and 
    #          postfix products.
    
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

# Time Complexity: O(n), where n is the length of the input list nums.
# We iterate through the list twice to calculate the prefix and postfix products.
# Space Complexity: O(n). We use a single list of size n to store the result.