class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Compare alpha and omega characters, approaching middle ground, if match not detected fail

        array = [y for y in str(x)] # convert to char array

        leftPointer = 0
        rightPointer = len(array) - 1

        while leftPointer < rightPointer:
            if array[leftPointer] == array[rightPointer]:
                leftPointer += 1
                rightPointer -= 1
            else:
                return False

        return True
