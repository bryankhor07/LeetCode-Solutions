def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    # Step 1: Create a hashmap to associate each height with its corresponding name
    hashmap = {}
    result = []  # Initialize the list to store the sorted names

    # Populate the hashmap with heights as keys and names as values
    for i in range(len(heights)):
        hashmap[heights[i]] = names[i]

    # Step 2: Sort the heights in descending order
    heights.sort(reverse=True)

    # Step 3: Build the result list using the sorted heights
    for i in range(len(names)):
        result.append(hashmap[heights[i]])

    # Step 4: Return the list of names sorted by descending heights
    return result

# Time complexity: O(nlogn), where n is the length of the input lists names and heights.
# The time complexity is dominated by the sorting operation on the heights.
# Space complexity: O(n), where n is the length of the input lists names and heights.