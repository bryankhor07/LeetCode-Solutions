def finalPrices(self, prices: List[int]) -> List[int]:
    stack = [] # Initialize a stack to store the prices.
    res = list(prices) # Initialize a list to store the final prices.

    # Iterate through the input list in reverse order.
    for i in range(len(prices) - 1, -1, -1):
        # While the stack is not empty and the top element is greater than the current price, pop the top element.
        while stack and stack[-1] > prices[i]:
            stack.pop()
        # If the stack is not empty, subtract the top element from the current price to get the final price.
        if stack:
            res[i] -= stack[-1]
        # Push the current price onto the stack.
        stack.append(prices[i])
    return res

# Time Complexity: O(n), where n is the length of the input list `prices`. We iterate through the list once.
# Space Complexity: O(n). The space complexity is due to the stack used to store the prices.