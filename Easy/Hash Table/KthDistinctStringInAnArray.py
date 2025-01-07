def kthDistinct(self, arr: List[str], k: int) -> str:
    # Step 1: Count occurrences
    count_map = {}
    for i, val in enumerate(arr):
        if val not in count_map:
            count_map[val] = 0
        count_map[val] += 1
    
    # Step 2: Filter distinct elements
    distinct_elements = [val for val in arr if count_map[val] == 1]
    
    # Step 3: Retrieve the k-th distinct element
    return distinct_elements[k - 1] if k <= len(distinct_elements) else ""

# Time complexity: O(n)
# Space complexity: O(n)