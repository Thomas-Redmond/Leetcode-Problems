class Solution:
    def romanToInt(self, s: str) -> int:

        # Using hashmap to store comparative values and special cases
        # Look at first char and check second to see if match special case: if so skip next char

        valid = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000, 'IV': 4, 'IX': 9, 'XL':40, 'XC':90, 'CD':400,
                 'CM':900}

        numChars = len(s)
        i = 0
        cumTotal = 0

        while i < numChars:
            if s[i:i+2] in valid:
                cumTotal += valid[s[i:i+2]]
                i+=2
            else:
                cumTotal += valid[s[i]]
                i+=1

        return cumTotal
