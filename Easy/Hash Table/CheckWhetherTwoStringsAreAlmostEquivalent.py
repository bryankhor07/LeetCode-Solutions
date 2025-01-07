def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
    # Create dictionaries to store character frequencies for both words
    hashmap1 = {}
    hashmap2 = {}

    # Count the frequency of each character in word1 and store it in hashmap1
    for char in word1:
        hashmap1[char] = 1 + hashmap1.get(char, 0)

    # Count the frequency of each character in word2 and store it in hashmap2
    for char in word2:
        hashmap2[char] = 1 + hashmap2.get(char, 0)

    # Compare frequencies of characters in hashmap1 with hashmap2
    # If a character exists in both hashmaps, check if the frequency difference exceeds 3
    # If a character exists only in hashmap1, ensure its frequency does not exceed 3
    for char, count in hashmap1.items():
        if char in hashmap2:
            if abs(hashmap2[char] - count) > 3:
                return False
        elif count > 3:
            return False

    # Compare frequencies of characters in hashmap2 with hashmap1
    # If a character exists in both hashmaps, check if the frequency difference exceeds 3
    # If a character exists only in hashmap2, ensure its frequency does not exceed 3
    for char, count in hashmap2.items():
        if char in hashmap1:
            if abs(hashmap1[char] - count) > 3:
                return False
        elif count > 3:
            return False

    # If all character frequency differences are within the allowed range, return True
    return True