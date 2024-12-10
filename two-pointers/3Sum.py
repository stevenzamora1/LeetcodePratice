class Solution:
    # Does not work with duplicates
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []

        low = 0
        high = len(nums) - 1

        for index in range(1, len(nums)-1):

            low = 0
            high = len(nums) - 1
            while (low < index and high > index):

                if ((nums[low] + nums[high] + nums[index]) == 0):

                    output.append([nums[low], nums[high], nums[index]])
                if ((nums[low] + nums[high] + nums[index]) < 0):
                    low += 1
                else:
                    high -= 1

        return output

    def threeSumSoultion(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort the array
        output = []

        for i, a in enumerate(nums):  # Fix one element at a time
            if a > 0:  # Break early if the fixed element is positive
                break

            # Skip duplicates for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1  # Two-pointer approach
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    output.append([a, nums[l], nums[r]])
                    # Skip duplicates for the pointers
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return output


obj = Solution()
print(obj.threeSum([0, 0, 0, 0]))
