class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        halfpoint = (left + right) // 2

        while left <= right:
            if nums[halfpoint] == target:
                return halfpoint

            if nums[halfpoint] > target:
                right = halfpoint - 1
                halfpoint = (left+right) // 2

            else:
                left = halfpoint + 1
                halfpoint = (left + right) // 2

            print(left, halfpoint, right)

        return -1


obj = Solution()
print(obj.search([-1, 0, 3, 5, 9, 12], 9))
