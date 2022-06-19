class Solution:
    def binarySearch(self, arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid

            elif arr[mid] > x:
                return self.binarySearch(arr, low, mid -1, x)
            else:
                return self.binarySearch(arr, mid+1, high, x)

        else:
            # element not found
            return low


    def searchInsert(self, nums: List[int], target: int) -> int:
        # implement binary search
        return self.binarySearch(nums, 0, len(nums) - 1, target)
