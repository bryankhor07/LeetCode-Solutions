def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = [] # Stack to store the asteroids

    # Iterate through the asteroids
    for asteroid in asteroids:
        # If the asteroid is positive or the stack is empty, append the asteroid to the stack
        # If the asteroid is negative, check for collisions with the asteroids in the stack
        # If there is a collision, remove the smaller asteroid(s) from the stack
        # If there is no collision, append the asteroid to the stack
        # Continue until the asteroid is positive or the stack is empty
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < abs(asteroid):
                stack.pop()
                continue
            elif stack[-1] == abs(asteroid):
                stack.pop()
            break
        else:
            stack.append(asteroid)
    return stack

# Time Complexity: O(n), where n is the number of asteroids in the input list.
# We iterate through each asteroid once.
# Space Complexity: O(n), where n is the number of asteroids in the input list.