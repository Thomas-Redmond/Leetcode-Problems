class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using left and right pointers, iterate through all values
        # comparing sum to see if they match target. When pointers move @ same position
        # move left over once, and reset rightPointer

        leftPointer = 0

        while leftPointer != len(nums) - 1:
            rightPointer = len(nums) - 1

            while rightPointer != leftPointer:
                if nums[leftPointer] + nums[rightPointer] == target:
                    # Presumes success
                    return [leftPointer, rightPointer]
                else:
                    # Decrement rightPointer
                    rightPointer = rightPointer - 1

            # Left value not used
            # Increment leftPointer
            leftPointer = leftPointer + 1
