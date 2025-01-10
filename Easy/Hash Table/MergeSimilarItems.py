def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    # Initialize a hashmap to store the weight sums for each unique value
    hashmap = {}
    ret = []  # This will hold the final sorted list of merged items

    # Iterate over items1 and populate the hashmap with value-weight pairs
    for i in range(len(items1)):
        # Add the weight to the corresponding value in the hashmap
        hashmap[items1[i][0]] = items1[i][1] + hashmap.get(items1[i][0], 0)

    # Iterate over items2 and do the same, adding weights for existing values
    for i in range(len(items2)):
        hashmap[items2[i][0]] = items2[i][1] + hashmap.get(items2[i][0], 0)

    # Convert the hashmap back into a list of [value, weight] pairs
    for key, value in hashmap.items():
        ret.append([key, value])

    # Sort the result by value
    ret.sort()

    # Return the sorted list
    return ret

# Time complexity: O(n + m + klog(k)), where n is the length of items1, m is the length of items2, and k is the number of unique values in both lists
# Space complexity: O(k), where k is the number of unique values in both lists