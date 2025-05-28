

def maxArea(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    maxi = 0

    while l != r:
        temp = min(height[l], height[r]) * (r - l)

        maxi = max(temp, maxi)
        if height[l] >= height[r]:
            r -= 1
        else:
            l += 1

    return maxi


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(maxArea([8, 7, 2, 1]))  # 7
