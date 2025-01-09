def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    # Sort both seats and students lists in ascending order
    # Sorting ensures we match the closest seat to each student to minimize the moves
    seats.sort()
    students.sort()
    
    # Initialize a counter to keep track of the total number of moves
    minNumOfMoves = 0

    # Iterate through each seat-student pair after sorting
    for i in range(len(seats)):
        # Calculate the absolute difference between the current seat and student positions
        # This represents the number of moves needed for the student to reach the seat
        minNumOfMoves += abs(seats[i] - students[i])
    
    # Return the total minimum number of moves required to seat all students
    return minNumOfMoves

# Time Complexity: O(nlogn) due to the sorting operation
# Space Complexity: O(1) since we are using a constant amount of space