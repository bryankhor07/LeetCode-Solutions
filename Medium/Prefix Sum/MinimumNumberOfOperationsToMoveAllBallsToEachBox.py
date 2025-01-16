def minOperations(self, boxes: str) -> List[int]:
    n = len(boxes)
    res = [0] * n
    prefix_count = 0  # Count of balls seen so far
    prefix_cost = 0   # Cumulative cost from the left

    # Pass from left to right
    for i in range(n):
        res[i] += prefix_cost
        if boxes[i] == '1':
            prefix_count += 1
        prefix_cost += prefix_count

    suffix_count = 0  # Count of balls seen so far
    suffix_cost = 0   # Cumulative cost from the right

    # Pass from right to left
    for i in range(n - 1, -1, -1):
        res[i] += suffix_cost
        if boxes[i] == '1':
            suffix_count += 1
        suffix_cost += suffix_count

    return res

# Time Complexity: O(n), where n is the length of the input string `boxes`.
# We perform two passes through the string `boxes`, once from left to right and once from right to left.
# Space Complexity: O(n). The space complexity is due to the list `res` used to store the result.