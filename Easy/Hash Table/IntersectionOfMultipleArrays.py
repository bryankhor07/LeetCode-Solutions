def intersection(self, nums: List[List[int]]) -> List[int]:
    # Create a hashmap to store the frequency of each number across all sublists
    hashmap = {}
    # Initialize an empty list to store the intersection result
    res = []

    # Iterate through each sublist in the input list
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            # Count the occurrences of each number across all sublists
            hashmap[nums[i][j]] = 1 + hashmap.get(nums[i][j], 0)

    # Iterate through the hashmap to identify numbers present in all sublists
    for key, value in hashmap.items():
        # If the frequency of a number equals the number of sublists,
        # it means the number is present in all sublists
        if value == len(nums):
            res.append(key)

    # Return the sorted list of numbers that are present in all sublists
    return sorted(res)

# Time Complexity: O(n * m) where n is the number of sublists and m is the average number of elements in each sublist
# Space Complexity: O(n * m) since the hashmap can store up to n * m elements