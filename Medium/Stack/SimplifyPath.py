def simplifyPath(self, path):
    # Split the input path by "/" to process each component separately
    res = path.split("/")
    # Stack to keep track of the valid directories in the simplified path
    stack = []
    # Variable to store the final simplified path
    finalRes = ""

    # Iterate through each component in the split path
    for i in range(len(res)):
        if res[i] == ".." and len(stack) != 0:
            # If the component is ".." and the stack is not empty,
            # move up one directory by popping the last directory from the stack
            stack.pop()
        elif res[i] == ".." and len(stack) == 0:
            # If the component is ".." and the stack is empty,
            # do nothing since there's no parent directory to move up to
            continue
        elif res[i] != "." and res[i] != "":
            # If the component is not "." (current directory) and not empty,
            # it's a valid directory name, so add it to the stack
            stack.append(res[i])

    # If the stack is empty after processing, the simplified path is just "/"
    if len(stack) == 0:
        finalRes = "/"
    else:
        # Otherwise, construct the simplified path by joining stack elements
        for i in range(len(stack)):
            finalRes += "/" + stack[i]

    # Return the final simplified path
    return finalRes

# Time Complexity: O(n), where n is the length of the input path. We iterate through each component in the path once.
# Space Complexity: O(n), where n is the length of the input path. The space complexity is due to the stack used to store the valid directories.