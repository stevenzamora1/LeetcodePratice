class Solution:
    def binarySearch(self, nums: list[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            midpoint = (low + high) // 2

            if nums[midpoint] == target:
                return midpoint
            if target > nums[midpoint]:
                low = midpoint + 1
            else:
                high = midpoint - 1
        return -1


obj = Solution()
print(obj.binarySearch([-10, -3, 0, 5, 9, 12], 20))
print(obj.binarySearch([-10, -3, 0, 5, 9, 12], 12))
print(obj.binarySearch([-10, -3, 0, 5, 9, 12], -3))
print(obj.binarySearch([-10, -3, 0, 5, 9, 12], 0))
