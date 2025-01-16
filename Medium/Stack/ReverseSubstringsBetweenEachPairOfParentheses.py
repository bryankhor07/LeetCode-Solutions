def reverseParentheses(self, s: str) -> str:
    open_parentheses_indices = []
    result = []

    for current_char in s:
        if current_char == "(":
            # Store the current length as the start index
            # for future reversal
            open_parentheses_indices.append(len(result))
        elif current_char == ")":
            start = open_parentheses_indices.pop()
            # Reverse the substring between the matching parentheses
            result[start:] = result[start:][::-1]
        else:
            # Append non-parenthesis characters to the processed list
            result.append(current_char)
    return "".join(result)

# Time Complexity: O(n^2), where n is the length of the input string `s`.
# In the worst case, we might have to reverse the entire string n times.
# This is because the string is reversed for each pair of matching parentheses.
# Space Complexity: O(n). The space complexity is due to the list `result` used to store the characters of the input string `s`.