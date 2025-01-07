def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    # Step 1: Pair each element with its index
    indexed_nums = list(enumerate(nums))  # [(index, value)]
    
    # Step 2: Sort by value in descending order and pick the top k elements
    top_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
    
    # Step 3: Sort the top k elements by their original indices to maintain order
    sorted_by_index = sorted(top_k, key=lambda x: x[0])
    
    # Step 4: Extract the values to form the subsequence
    return [x[1] for x in sorted_by_index]

# Time complexity: O(nlogn)
# Space complexity: O(n)