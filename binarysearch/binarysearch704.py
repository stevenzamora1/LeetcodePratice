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


print(searchMatrix([[1, 3, 5, 7],
                   [10, 11, 16, 20],
                   [23, 30, 34, 60]], 3))  # true
print(searchMatrix([[1, 3, 5, 7],
                   [10, 11, 16, 20],
                   [23, 30, 34, 60]], 13))  # false
