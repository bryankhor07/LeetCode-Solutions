def minOperations(self, logs: List[str]) -> int:
    stack = [] # Stack to store directories

    # Iterate through the logs list to simulate the crawler
    for i in range(len(logs)):
        # If the current directory is '../', move up one level in the directory structure
        if stack and logs[i] == "../":
            stack.pop()
        # If the current directory is './', stay in the current directory
        elif logs[i] == "./":
            continue
        # Otherwise, add the current directory to the stack
        elif logs[i] != "../":
            stack.append(logs[i])
    return len(stack)

# Time Complexity: O(n), where n is the length of the input list `logs`.
# Space Complexity: O(n). The space complexity is due to the stack used to store the directories.