class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxValue = n = 0
        j = len(height) - 1
        while n != j:
            print("start of loop", n, j)
            tempValue = (j - n) * min(height[j], height[n])
            res = max(res, tempValue)
            if height[j] <= height[n]:
                j -= 1

            else:
                n += 1

        return maxValue


obj = Solution()
print(obj.maxArea([1, 2, 1]))
