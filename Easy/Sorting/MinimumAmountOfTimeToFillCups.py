def fillCups(self, amount: List[int]) -> int:
    seconds = 0

    while sum(amount) > 0:  # Continue until all amounts are zero
        amount.sort(reverse=True)  # Sort in descending order
        if amount[0] > 0 and amount[1] > 0:
            # Decrement the two largest values
            amount[0] -= 1
            amount[1] -= 1
        else:
            # If only one non-zero element is left, decrement it
            amount[0] -= 1
        seconds += 1

    return seconds

# Time complexity: O(n^2logn), where n is the length of the input list amount.
# The while loop runs until all elements in the list are zero, and each iteration
# involves sorting the list, which has a time complexity of O(nlogn).
# Space complexity: O(1), as the algorithm uses a constant amount of extra space