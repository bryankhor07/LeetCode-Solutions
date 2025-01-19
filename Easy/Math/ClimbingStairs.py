def climbStairs(self, n: int) -> int:
    arr = [0] * (n + 1) # List to store the number of ways to climb the stairs.
    arr[0] = arr[1] = 1 # Base case: 1 way to climb 0 or 1 stair.

    # Calculate the number of ways to climb the stairs.
    # The number of ways to climb the stairs at step i is the sum of the number of ways to climb the stairs at step i-1 and i-2.
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

# Time Complexity: O(n), where n is the input number n.
# We iterate through the list once to calculate the number of ways to climb the stairs.
# Space Complexity: O(n). We use a list of size n to store the number of ways to climb the stairs.