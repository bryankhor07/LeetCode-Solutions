def countPoints(self, rings: str) -> int:
    # Create dictionaries to track the presence of blue, red, and green rings for each rod
    blueRings = {}
    redRings = {}
    greenRings = {}
    
    # Initialize a counter for rods that have all three ring colors
    count = 0

    # Iterate through the rings string in steps of 2 (color and rod number)
    for i in range(0, len(rings), 2):
        # Extract the color and rod number
        color = rings[i]
        rod = int(rings[i + 1])
        
        # Update the respective dictionary based on the color
        if color == 'B':  # Blue ring
            blueRings[rod] = 1
        elif color == 'R':  # Red ring
            redRings[rod] = 1
        else:  # Green ring
            greenRings[rod] = 1

    # Check each rod (from 0 to 9) to see if it has all three ring colors
    for i in range(10):
        if i in blueRings and i in redRings and i in greenRings:
            count += 1  # Increment the counter if the rod has all three colors
    
    # Return the total number of rods with all three ring colors
    return count

# Time Complexity: O(n)
# Space Complexity: O(1) since the size of the dictionaries is constant