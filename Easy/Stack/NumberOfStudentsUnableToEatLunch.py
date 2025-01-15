def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    res = len(students) # Initialize the result to the length of the students list
    count = Counter(students) # Count the number of each type of student

    # Iterate through the sandwiches list
    for s in sandwiches:
        # If the count of the current type of student is greater than 0, decrement the result and decrement the count of the current type of student
        if count[s] > 0:
            res -= 1
            count[s] -= 1
        # Otherwise, return the result
        else:
            return res
    return res

# Time Complexity: O(n), where n is the length of the input list `students`. We iterate through the list once.
# Space Complexity: O(n). The space complexity is due to the counter used to store the count of each type of student.