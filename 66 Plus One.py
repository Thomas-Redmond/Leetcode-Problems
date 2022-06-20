class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Using Recursion
        # if array empty insert 0
        # elif last digit now 10, apply recursion
        # else just add one

        if len(digits) == 0:
            digits.insert(0, 1)

        elif digits[-1] == 9:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])

        else:
            digits[-1] += 1

        return digits
