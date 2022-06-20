class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # decrement from end of string s, incrementing counter until a space is reached

        endPointer = len(s) - 1
        if s[endPointer] == ' ':
            # space detected at end. skip to first word
            while s[endPointer] == ' ':
                endPointer -= 1

        counter = 0
        while endPointer >= 0 and s[endPointer] != ' ':
            counter += 1
            endPointer -= 1

        return counter
