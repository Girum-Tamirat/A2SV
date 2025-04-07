# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)  # Get the length of the string

        # Step 1: Initialize a difference array with zeros
        diff_array = [0] * n  

        # Step 2: Process each shift operation
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                diff_array[start] += 1  # Increase shift at the start index
                if end + 1 < n:
                    diff_array[end + 1] -= 1  # Neutralize shift after the end index
            else:  # Backward shift
                diff_array[start] -= 1  # Decrease shift at the start index
                if end + 1 < n:
                    diff_array[end + 1] += 1  # Neutralize shift after the end index

        # Step 3: Compute cumulative shifts
        cumulative_shift = 0
        result = list(s)  # Convert string to a list for mutability

        for i in range(n):
            cumulative_shift = (cumulative_shift + diff_array[i]) % 26  # Apply shift within bounds
            if cumulative_shift < 0:
                cumulative_shift += 26  # Handle negative shift values

            # Shift the current character
            new_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result[i] = new_char  # Update the character

        return "".join(result)  # Convert list back to a string
