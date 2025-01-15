def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    op = ['+', '-', '*', '/']
    for t in tokens:
        # If an operator is encountered, pop the top 2 elements in the stack
        # and calculate the value corresponding to the operator and append it
        # back to the stack. Else, append the number to the stack.
        if t in op:
            x, y = int(stack.pop()), int(stack.pop())
            if t == '+':
                stack.append(x + y)
            elif t == '-':
                stack.append(y- x)
            elif t == '*':
                stack.append(x * y)
            else:
                stack.append(int(y / x))
        else:
            stack.append(t)
    return int(stack[-1])

# Time Complexity: O(n), where n is the number of elements in the input list `tokens`.
# We iterate through each element in the list once.
# Space Complexity: O(n), where n is the number of elements in the input list `tokens`.