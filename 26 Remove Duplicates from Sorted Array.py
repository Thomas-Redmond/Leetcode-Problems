class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Remove duplicates from sorted array retaining relative order
        # Retain length of array, and have only O(1) space complexity

        # Test index, compare with next index
        # If same apply pointer 'deletion' at duplicate continue through list
        # until find next non duplicate, replace at 'deletion', increment deletion pointer

        insertPointer = 0
        i = 0
        cur = nums[i]

        while i < len(nums) - 1:

            if cur != nums[i+1]:
                insertPointer += 1
                i += 1

                cur = nums[i]
                nums[insertPointer] = cur

            else:
                # cur stays same
                i += 1

        return insertPointer + 1
