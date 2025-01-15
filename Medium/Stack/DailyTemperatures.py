def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    # In the stack, I'll be storing a pair of values temp and index 
    # The index will be used to calculate the number of days it took to 
    # find a greater temperature.
    stack = [] # pair: [temp, index]

    # I'm going to enumerate through the array which means that
    # I'm going to get the index and value from the array at the same time.
    for i, t in enumerate(temperatures):
        # First I'm going to check if the stack is empty and if it is,
        # is this temperature greater than the temperature on top of our stack
        while stack and t > stack[-1][0]:
            stackT, stackIndex = stack.pop()
            # Calculate the number of days it took to reach a higher temperature
            # by taking the current index i and minus the index I just popped from the stack
            res[stackIndex] = (i - stackIndex)
        stack.append([t, i])
    return res

# Time Complexity: O(n), where n is the number of temperatures in the input list.
# We iterate through each temperature once.
# Space Complexity: O(n), where n is the number of temperatures in the input list.