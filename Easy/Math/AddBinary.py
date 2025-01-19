def addBinary(self, a: str, b: str) -> str:
    sb = []  # Using a list to build the result string
    i = len(a) - 1
    j = len(b) - 1
    carry = 0

    while i >= 0 or j >= 0:
        sum_val = carry
        if i >= 0:
            sum_val += int(a[i])  # Convert character to integer
        if j >= 0:
            sum_val += int(b[j])

        sb.append(str(sum_val % 2))  # Append the remainder (0 or 1) to the result
        carry = sum_val // 2  # Calculate carry for the next column

        i -= 1
        j -= 1

    if carry != 0:  # If there's a leftover carry, append it
        sb.append(str(carry))

    return ''.join(sb[::-1])  # Reverse the list and join to form the final string

# Time Complexity: O(max(n, m)), where n and m are the lengths of the input strings a and b.
# We iterate through both strings once to perform the binary addition.
# Space Complexity: O(max(n, m)). We use a list of size max(n, m) to store the result.