# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        # Check each row for any repetition. Return false if there are repetitions.
        for i in range(9):
            for j in range(9):
                current_num = board[i][j]
            
                # Check if the number is already present in the set
                if current_num in seen:
                    return False
                # Only add the string if it is a digit
                if current_num.isdigit():
                    seen.add(current_num)
            seen = set() # Reset the set to empty
    
        seen = set() # Reset the set to empty
    
        # Check each column for any repetition. Return false if there are repetitions.
        for i in range(9):
            for j in range(9):
                current_num = board[j][i]
            
                # Check if the number is already present in the set
                if current_num in seen:
                    return False
                # Only add the string if it is a digit
                if current_num.isdigit():
                    seen.add(current_num)
            seen = set() # Reset the set to empty
    
        seen = set() # Reset the set to empty
        for start_row in range(0, 9, 3):  # Iterate over the starting row indices of subgrids
            for start_col in range(0, 9, 3):  # Iterate over the starting column indices of subgrids
                seen = set()
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        current_num = board[i][j]
                    
                        # Check if the number is already present in the set
                        if current_num in seen:
                            return False
                        # Only add the string if it is a digit
                        if current_num.isdigit():
                            seen.add(current_num)
                seen = set() # Reset the set to empty
        return True
