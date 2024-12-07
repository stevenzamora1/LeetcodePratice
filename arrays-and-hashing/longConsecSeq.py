class Solution:

    # In my first attempt I started if any number was Consecutive and it went over the max runtime
    # In my second attempt i ONLY started at the start of a sequence

    def longestConsecutiveFirstAttempt(self, nums: list[int]) -> int:
        my_set = set(nums)
        longestSet = set()
        if len(nums) == 0:
            return 0
        longestStreak = 1
        for n in nums:
            tempStreak = 0
            if (n + 1) in my_set and n not in longestSet:
                while (n+tempStreak) in my_set:
                    longestSet.add(n+tempStreak)
                    tempStreak += 1
                if tempStreak > longestStreak:
                    longestStreak = tempStreak

        return longestStreak

    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        my_set = set(nums)
        longestStreak = 1

        for n in my_set:  # Iterate over the set directly to avoid duplicates in nums
            if (n - 1) not in my_set:  # Start only at the beginning of a streak
                tempStreak = 1
                while (n + tempStreak) in my_set:
                    tempStreak += 1
                    if tempStreak > longestStreak:
                        longestStreak = tempStreak

        return longestStreak


obj = Solution()

print(obj.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
