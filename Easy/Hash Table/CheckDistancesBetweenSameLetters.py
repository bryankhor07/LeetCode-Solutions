def checkDistances(self, s: str, distance: List[int]) -> bool:
    hashmap = {}  # Dictionary to store the first occurrence index of each character.

    for i in range(len(s)):
        # Check if the character has been seen before.
        if s[i] in hashmap:
            # Calculate the index in the distance array for the current character.
            distanceIndex = ord(s[i]) - ord('a')
            # Verify if the calculated distance matches the expected distance.
            # i - hashmap[s[i]] - 1 gives the number of characters between the two occurrences.
            if i - hashmap[s[i]] - 1 != distance[distanceIndex]:
                return False  # Return False if the condition is not satisfied.
        else:
            # Store the index of the first occurrence of the character.
            hashmap[s[i]] = i
    return True  # Return True if all distance checks pass.

# Time complexity: O(n), where n is the length of the input string s.
# Space complexity: O(1) since the hashmap will store at most 26 characters.