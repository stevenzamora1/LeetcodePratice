# Since the input array is sorted use binary search
# to find if there is a second index

def twoSum(numbers: list[int], target: int) -> list[int]:

    for index, num in enumerate(numbers):
        findSecond = target - num
        secondNumFound = binarySearch(numbers, findSecond, index)
        if secondNumFound == -1:
            continue
        else:
            return ([index + 1, secondNumFound + 1])

# helper function


def binarySearch(numbers: list[int], target: int) -> int:
    output = -1
    low = 0
    high = len(numbers) - 1
    midpoint = (low + high) // 2

    while low <= high:

        if numbers[midpoint] == target:
            return midpoint
        if numbers[midpoint] < target:
            low = midpoint + 1
            midpoint = (low + high) // 2
        else:
            high = midpoint - 1
            midpoint = (low + high) // 2

    return output

# uses a simple two pointer approach no bineary serach


def twoSumSimpleSearch(numbers: list[int], target: int) -> list[int]:
    low = 0
    high = len(numbers) - 1
    while (low < high):
        foundTarget = numbers[high] + numbers[low]
        if foundTarget == target:
            return [low + 1, high + 1]
        elif foundTarget < target:
            low += 1
        else:
            high -= 1


# given an integer array height of length n.
# There are n vertical lines drawn such that the two
# endpoints of the ith line are (i, 0) and (i, height[i])
def maxArea(height: list[int]) -> int:
    maxWataer = 0
    left = 0
    right = len(height) - 1
    while (left < right):
        length = min(height[left], height[right])
        maxWataer = max(maxWataer, length * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxWataer

# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    top = 0
    bottom = len(matrix) - 1
    midpoint = (top + bottom) // 2

    while (top <= bottom):

        if matrix[midpoint][0] > target:
            bottom = midpoint - 1
            midpoint = (top + bottom) // 2

        elif matrix[midpoint][len(matrix[midpoint]) - 1] < target:
            top = midpoint + 1
            midpoint = (top + bottom) // 2

        elif matrix[midpoint][0] <= target and matrix[midpoint][-1] >= target:
            return binarySearch(matrix[midpoint], target) != -1


print(searchMatrix([[1, 3, 5, 7],
                   [10, 11, 16, 20],
                   [23, 30, 34, 60]], 3))  # true
print(searchMatrix([[1, 3, 5, 7],
                   [10, 11, 16, 20],
                   [23, 30, 34, 60]], 13))  # false


# print(twoSum([2, 7, 11, 15], 9))  # [1,2]
# print(twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))  # [1,2]
# print(twoSumSimpleSearch([1, 2, 3, 4, 4, 9, 56, 90], 8))  # [1,2]
# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
# print(maxArea([1, 1]))  # 1
