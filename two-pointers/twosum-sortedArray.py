# Given a 1-indexed array

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low = 0
        high = len(numbers) - 1
        while (low < high):
            currentSum = numbers[low] + numbers[high]
            if (currentSum == target):
                return [(low+1), (high+1)]
            elif (currentSum < target):
                low += 1
            elif (currentSum > target):
                high -= 1


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))  # output [1, 2]
print(obj.twoSum([2, 3, 4], 6))  # output[1, 3]
print(obj.twoSum([-1, 0], -1))  # output[1, 2]
