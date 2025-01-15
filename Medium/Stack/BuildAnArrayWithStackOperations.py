def buildArray(self, target: List[int], n: int) -> List[str]:
    stackOps = [] # List to store the stack operations
    targetIndex = 0
    i = 1

    # Iterate through the numbers from 1 to n and compare with the target list
    while i < n + 1 and targetIndex < len(target):
        # If the current number is equal to the target number, push the operation to the stack and increment the target index
        if target[targetIndex] == i:
            stackOps.append("Push")
            targetIndex += 1
        # If the current number is not equal to the target number, push the operations "Push" and "Pop" to the stack
        elif target[targetIndex] != i:
            stackOps.append("Push")
            stackOps.append("Pop")
        i += 1
    return stackOps

# Time Complexity: O(n), where n is the length of the input list `target`. We iterate through the list once.
# Space Complexity: O(n). The space complexity is due to the stackOps list used to store the stack operations.