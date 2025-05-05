
class Solution:

    # First Attempt a couple of months ago
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_return = []

        for x in nums:

            first_index = nums.index(x)
            second_target = target - x

            if second_target in nums and second_target != x:

                second_index = nums.index(second_target)
                nums_return.append(first_index)
                nums_return.append(second_index)

                return nums_return

        return nums_return

    # Second attempt right
    def twoSum(nums: list[int], target: int) -> list[int]:
        hashMap = {}
        for n in range(0, len(nums)):
            found = target - nums[n]
            if nums[n] in hashMap:
                return [n, hashMap.get(nums[n])]
            hashMap[found] = n


obj = Solution()
print(obj.twoSum([3, 3], 6))
