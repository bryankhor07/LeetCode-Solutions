def calPoints(self, operations: List[str]) -> int:
    stack = [] # Stack to store scores

    # Iterate through the operations list to calculate the total score
    for i in range(len(operations)):
        # If the current operation is 'C', remove the last valid score
        # If the current operation is 'D', double the last valid score
        # If the current operation is '+', add the sum of the last two valid scores
        # Otherwise, add the current score to the stack
        if operations[i] == '+':
            stack.append(stack[-1] + stack[-2])
        elif operations[i] == 'D':
            stack.append(stack[-1] * 2)
        elif operations[i] == 'C':
            stack.pop()
        else:
            stack.append(int(operations[i]))
    return sum(stack)

# Time Complexity: O(n), where n is the length of the input list `operations`.
# Space Complexity: O(n). The space complexity is due to the stack used to store the scores