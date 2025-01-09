def wordPattern(self, pattern: str, s: str) -> bool:
    # Split the input string `s` into a list of words
    sList = s.split(" ")

    # If the lengths of `pattern` and `sList` do not match, the pattern cannot match
    if len(pattern) != len(sList):
        return False

    # Create two hashmaps for bidirectional mapping
    char_to_word = {}
    word_to_char = {}

    # Iterate through the pattern and corresponding words
    for i in range(len(pattern)):
        char = pattern[i]
        word = sList[i]

        # Check if the character is already mapped to a word
        if char in char_to_word:
            if char_to_word[char] != word:  # If the mapping doesn't match, return False
                return False
        else:
            char_to_word[char] = word  # Map the character to the word

        # Check if the word is already mapped to a character
        if word in word_to_char:
            if word_to_char[word] != char:  # If the mapping doesn't match, return False
                return False
        else:
            word_to_char[word] = char  # Map the word to the character

    # If all checks pass, return True
    return True

# Time Complexity: O(n) where n is the length of the input string `s`
# Space Complexity: O(n) since we store the mappings of characters to words and vice versa