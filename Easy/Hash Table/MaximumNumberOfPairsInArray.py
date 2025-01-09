def numberOfPairs(self, nums: List[int]) -> List[int]:
    # Initialize a dictionary to store the frequency of each number
    freq = {}
    
    # Initialize the result list to store the number of pairs and leftovers
    # res[0] will store the count of pairs
    # res[1] will store the count of leftover elements
    res = [0] * 2

    # Count the frequency of each number in nums
    for num in nums:
        freq[num] = 1 + freq.get(num, 0)  # Increment the frequency of the current number

    # Calculate the number of pairs and leftovers for each number
    for key, val in freq.items():
        if val % 2 == 0:
            # If the frequency is even, all instances can form pairs
            res[0] += (val // 2)  # Add the number of pairs to res[0]
        else:
            # If the frequency is odd, one instance will be leftover
            res[0] += ((val - 1) // 2)  # Add the number of pairs to res[0]
            res[1] += 1  # Add the leftover count to res[1]

    # Return the result: [number of pairs, number of leftovers]
    return res

# Time Complexity: O(n) where n is the number of elements in the input list
# Space Complexity: O(n) since we store all the elements in the input list in a dictionary