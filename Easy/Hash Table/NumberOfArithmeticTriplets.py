def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
    # Initialize a hashmap to store each number as a key and its index as the value
    hashmap = {}
    count = 0  # Variable to keep track of the number of valid arithmetic triplets

    # Populate the hashmap with the numbers and their indices
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    # Check for valid arithmetic triplets
    for num in nums:
        # If both (num - diff) and (num + diff) exist in the hashmap, we have a triplet
        if (num - diff) in hashmap and (num + diff) in hashmap:
            count += 1

    # Return the total count of arithmetic triplets found
    return count

# Time complexity: O(n)
# Space complexity: O(n) where n is the length of the input list nums