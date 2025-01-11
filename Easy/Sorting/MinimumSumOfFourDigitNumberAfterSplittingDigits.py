def minimumSum(self, num: int) -> int:
    numList = []  # List to store individual digits of the number.
    new1 = new2 = ""  # Strings to construct the two new numbers.

    # Extract digits from the number and store them in numList.
    while num > 0:
        digit = num % 10  # Get the last digit.
        numList.append(digit)  # Add it to the list.
        num = num // 10  # Remove the last digit from num.

    # Sort the digits in ascending order.
    numsSorted = sorted(numList)

    # Combine digits into two new numbers to minimize their sum.
    for i in range(0, len(numsSorted), 2):
        new1 += str(numsSorted[i])  # Add the smaller digit to the first number.
        new2 += str(numsSorted[i + 1])  # Add the next smaller digit to the second number.

    # Convert the two numbers to integers, compute their sum, and return it.
    return int(new1) + int(new2)

# Time complexity: O(nlogn), where n is the number of digits in the input number.
# The time complexity is dominated by the sorting operation.
# Space complexity: O(n), where n is the number of digits in the input number.