# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False
        elif n == 0:
            return True
      
        # Get the number of digits
        num_digits = math.floor(math.log10(n)) + 1
        position_tracker = 1
        temp_n = n
        # Iterate only half the number of digits
        for i in range(num_digits // 2):
           # Get the left digit
           left_most_digit = (n // 10**(num_digits - position_tracker)) % 10
           # Get the right digit
           right_most_digit = temp_n % 10
           if left_most_digit != right_most_digit:
              return False
           # Update temp_n by removing the right_most digit
           temp_n = temp_n // 10
           # Update position tracker 
           position_tracker += 1
   
        return True
