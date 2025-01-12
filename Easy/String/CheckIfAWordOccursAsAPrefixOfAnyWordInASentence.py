def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    # Split the sentence into words
    sentenceList = sentence.split(" ")

    # Iterate over the words with their indices
    for i, word in enumerate(sentenceList):
        # Check if the current word starts with the search word
        if word.startswith(searchWord):
            return i + 1

    # If no word matches, return -1
    return -1

# Time Complexity: O(n * m), where n is the number of words in the sentence and m is the length of the search word.
# Space Complexity: O(n), where n is the number of words in the sentence. The space complexity is due to the split sentenceList.