class Solution:
    def isValid(self, s: str) -> bool:
        # Put opening bracket in stack, popped when closing bracket met

        bracketPairs = {'(':')', '{':'}', '[':']'}
        stack = []

        for x in s:
            if x in bracketPairs:
                # Add opening bracket to top of stack
                stack.append(x)
            elif len(stack) == 0:
                # Given above bracket must be closing, and have no opening
                return False
            else:
                if bracketPairs[stack.pop()] != x:
                    # if closing bracket does not close last opening bracket
                    # Or beginning with a closing bracket
                    return False

        if len(stack) == 0:
            return True
        else: return False # not all brackets terminated
