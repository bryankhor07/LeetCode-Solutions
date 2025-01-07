def countKDifference(self, nums: List[int], k: int) -> int:
    hashmap = {}  # val : count of occurrences
    count = 0

    for num in nums:
        # Check if there exists a number that satisfies the absolute difference condition
        if num + k in hashmap:
            count += hashmap[num + k]
        if num - k in hashmap:
            count += hashmap[num - k]
        
        # Update the hashmap with the current number
        hashmap[num] = hashmap.get(num, 0) + 1

    return count

# Time Complexity: O(n)
# Space Complexity: O(n)