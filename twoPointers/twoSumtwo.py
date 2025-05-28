def twoSum(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1

    while l < r:

        if target - numbers[l] == numbers[r]:

            return [l + 1, r + 1]
        if target - numbers[l] > numbers[r]:
            l += 1
        else:
            r -= 1


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
print(twoSum([-1, 0], -1))
