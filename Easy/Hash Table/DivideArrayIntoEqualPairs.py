def divideArray(self, nums: List[int]) -> bool:
    # Create a hashmap to count the frequency of each number in the list
    hashmap = {}

    # Iterate through the list and populate the hashmap
    for n in nums:
        # Increment the count for each number, initializing to 1 if it doesn't exist
        hashmap[n] = 1 + hashmap.get(n, 0)

    # Check the frequency of each number in the hashmap
    for value in hashmap.values():
        # If any number has an odd frequency, it cannot form pairs
        if value % 2 != 0:
            return False

    # If all numbers have even frequencies, return True
    return True

# Time Complexity: O(n) where n is the number of elements in the input list
# Space Complexity: O(n) since we store all the elements in the input list in a hashmap