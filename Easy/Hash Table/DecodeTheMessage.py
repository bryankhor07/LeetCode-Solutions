def decodeMessage(self, key: str, message: str) -> str:
    # Initialize a dictionary to map each character in the key to a decoded character
    hashmap = {}
    
    # Initialize an empty string to store the decoded message
    res = ""
    
    # ASCII value for 'a' (start of the lowercase alphabet)
    asciiValue = 97  # ASCII value for 'a'
    
    # Index to iterate through the key
    i = 0

    # Create a mapping from unique characters in the key to the alphabet
    while i < len(key) and asciiValue <= 122:  # Loop until all letters ('a' to 'z') are mapped
        # Skip spaces and already-mapped characters in the key
        if key[i] == " " or key[i] in hashmap:
            i += 1
            continue

        # Map the current character in the key to the next letter in the alphabet
        hashmap[key[i]] = chr(asciiValue)
        
        # Move to the next letter in the alphabet
        asciiValue += 1
        
        # Move to the next character in the key
        i += 1

    # Decode the message using the mapping
    for i in range(len(message)):
        if message[i] == " ":  # Preserve spaces in the message
            res += " "
        else:
            res += hashmap[message[i]]  # Replace each character with its mapped value

    # Return the fully decoded message
    return res

# Time Complexity: O(n + m) where n is the length of the key and m is the length of the message
# Space Complexity: O(1) since the size of the hashmap is fixed (26 characters) regardless of the input size