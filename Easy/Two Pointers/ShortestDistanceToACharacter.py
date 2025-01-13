def shortestToChar(self, s: str, c: str) -> List[int]:
    """
    This function calculates the shortest distance from each character in a string `s`
    to a given target character `c`.
    
    Parameters:
    s (str): The input string.
    c (str): The target character to calculate distances to.
    
    Returns:
    List[int]: A list where each index contains the shortest distance from the character
               at that index in `s` to the nearest occurrence of `c`.
    """

    n = len(s)  # Length of the input string
    left, right, output = [None] * n, [None] * n, [None] * n  # Arrays to store distances from the left, right, and final result

    temp = float('inf')  # Initialize `temp` as infinity to represent no occurrence of `c` found yet

    # Pass 1: Calculate distances from the left
    for i in range(n):
        if s[i] == c:  # If the current character matches `c`, reset distance
            temp = 0
        left[i] = temp  # Store the distance from the left
        temp += 1  # Increment distance for subsequent characters

    temp = float('inf')  # Reset `temp` for the second pass

    # Pass 2: Calculate distances from the right
    for i in range(n - 1, -1, -1):  # Traverse the string from right to left
        if s[i] == c:  # If the current character matches `c`, reset distance
            temp = 0
        right[i] = temp  # Store the distance from the right
        temp += 1  # Increment distance for subsequent characters

    # Pass 3: Combine results from both passes
    for i in range(n):
        output[i] = min(left[i], right[i])  # Take the minimum distance from either side

    return output  # Return the list of shortest distances

# Time Complexity: O(n), where n is the length of the input string s.
# Space Complexity: O(n), where n is the length of the input string s. The space complexity is due to the three arrays used to store the distances from the left, right, and the final result.