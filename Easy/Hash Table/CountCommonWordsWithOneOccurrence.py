def countWords(self, words1: List[str], words2: List[str]) -> int:
    hashmap1 = {} 
    hashmap2 = {}
    count = 0

    # Iterate both arrays and store their frequency in a hashmap
    for i in range(len(words1)):
        hashmap1[words1[i]] = 1 + hashmap1.get(words1[i], 0)
    
    for i in range(len(words2)):
        hashmap2[words2[i]] = 1 + hashmap2.get(words2[i], 0)

    # Check if the word exists in both hashmaps and that their frequency is 1
    for key, val in hashmap1.items():
        if key in hashmap2 and val == 1 and hashmap2[key] == 1:
            count += 1
    
    return count

# Time complexity: O(n)
# Space complexity: O(n)