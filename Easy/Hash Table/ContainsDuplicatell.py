def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # Create a hashmap to store the most recent index of each number in the list
    hashmap = {}

    # Iterate through the list to check for nearby duplicates
    for i in range(len(nums)):
        # If the current number already exists in the hashmap
        if nums[i] in hashmap:
            # Check if the difference between indices is less than or equal to k
            if abs(hashmap[nums[i]] - i) <= k:
                return True  # A nearby duplicate is found
            else:
                # Update the index of the current number to the latest occurrence
                hashmap[nums[i]] = i
        else:
            # If the number is not in the hashmap, add it with its current index
            hashmap[nums[i]] = i

    # If no nearby duplicates are found, return False
    return False

# Time Complexity: O(n) since we loop through the array once
# Space Complexity: O(n) since the hashmap can store up to n elements