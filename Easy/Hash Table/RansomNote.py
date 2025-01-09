def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # Initialize dictionaries to store character frequencies
    hashmap1 = {}  # To count characters in ransomNote
    hashmap2 = {}  # To count characters in magazine

    # Count the frequency of each character in ransomNote
    for i in range(len(ransomNote)):
        hashmap1[ransomNote[i]] = 1 + hashmap1.get(ransomNote[i], 0)

    # Count the frequency of each character in magazine
    for i in range(len(magazine)):
        hashmap2[magazine[i]] = 1 + hashmap2.get(magazine[i], 0)

    # Check if each character in ransomNote can be constructed using magazine
    for key, val in hashmap1.items():
        if key in hashmap2 and hashmap2[key] < val:
            # If the character exists in magazine but not in sufficient quantity
            return False
        elif key not in hashmap2:
            # If the character doesn't exist in magazine
            return False

    # If all characters in ransomNote can be constructed from magazine
    return True

# Time Complexity: O(n + m) where n is the length of ransomNote and m is the length of magazine
# Space Complexity: O(n + m) since we store the frequencies of characters in ransomNote and magazine