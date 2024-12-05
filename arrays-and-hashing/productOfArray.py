class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            output[i] = pref[i] * suff[i]

        return output


obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))

# output should be [24, 12, 8 ,6]

# Create two arrays , one prefix array another postfix array
