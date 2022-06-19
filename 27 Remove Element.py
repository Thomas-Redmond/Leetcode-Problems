class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        knownGood = 0

        while i < len(nums):
            if nums[i] == val:
                # Found undesirable value
                i += 1
            else:
                # Found Good value
                nums[knownGood] = nums[i]   # Replace last known bad with latest good
                knownGood += 1              # Increment knownGood to now point next to knownGood
                i +=1

        return knownGood
