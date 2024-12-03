class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = [[] for i in range(len(nums) + 1)]

        listMap = {}

    # Hashmap to count how many times each value in nums occurs
        for n in nums:
            if n in listMap:
                listMap[n] += 1
            else:
                listMap[n] = 1

    # makes the values the indices in the freq array
    # For example if 1 shows up 3 times then in the freq array
    # at index 3 we will have [1]
        for n, c in listMap.items():
            freq[c].append(n)

        result = []

    # Goes backwards from thr freq array k times to get answer
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result


obj = Solution()
print(obj.topKFrequent([1, 1, 1, 2, 2, 3], 2))


# Uses a version of bucket sort
