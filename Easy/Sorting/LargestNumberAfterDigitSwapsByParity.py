def largestInteger(self, num: int) -> int:
    # Separate lists to store even and odd digits
    evenList = []
    oddList = []
    numCopy = num  # Create a copy of the input number for processing
    numArr = []  # List to store the digits of the number
    res = ""  # String to build the resulting number

    # Extract digits from the number and group them into even and odd lists
    while numCopy > 0:
        digit = numCopy % 10  # Get the last digit
        numArr.append(digit)  # Add the digit to numArr
        numCopy = numCopy // 10  # Remove the last digit from numCopy
        if digit % 2 == 0:  # Check if the digit is even
            evenList.append(digit)  # Add to even list
        else:  # Otherwise, it is odd
            oddList.append(digit)  # Add to odd list

    # Sort even and odd lists in descending order to maximize the result
    sortedEvenList = sorted(evenList, reverse=True)
    sortedOddList = sorted(oddList, reverse=True)
    evenIndex = oddIndex = 0  # Pointers to track positions in sorted lists

    # Rebuild the number while preserving the parity of each position
    for i in range(len(numArr)-1, -1, -1):  # Iterate through numArr in reverse
        if numArr[i] % 2 == 0:  # If the digit is even
            res += str(sortedEvenList[evenIndex])  # Append the largest remaining even digit
            evenIndex += 1  # Move to the next even digit
        else:  # If the digit is odd
            res += str(sortedOddList[oddIndex])  # Append the largest remaining odd digit
            oddIndex += 1  # Move to the next odd digit

    # Convert the resulting string back to an integer and return it
    return int(res)

# Time complexity: O(nlogn), where n is the number of digits in the input number.
# The time complexity is dominated by the sorting operation.
# Space complexity: O(n), where n is the number of digits in the input number.