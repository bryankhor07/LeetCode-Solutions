def largestAltitude(self, gain: List[int]) -> int:
    # Initialize the highest altitude as 0 (starting point)
    highest = 0

    # Initialize an altitudes list with the starting altitude of 0
    altitudes = [0] * (len(gain) + 1)

    # Iterate through the gain list to calculate the altitudes
    for i in range(1, len(altitudes)):
        # Calculate the current altitude based on the previous altitude and the current gain
        altitudes[i] = altitudes[i - 1] + gain[i - 1]
        # Update the highest altitude encountered so far
        highest = max(highest, altitudes[i])
    return highest

# Time Complexity: O(n), where n is the length of the input list gain.
# We iterate through the list once to calculate the altitudes.
# Space Complexity: O(n). We use an additional list of size n to store