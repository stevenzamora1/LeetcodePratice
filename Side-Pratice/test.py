def topKFrequent(nums: list[int], k: int) -> list[int]:
    hashTable = {}
    freq = [[] for i in range(len(nums))]

    for n in nums:
        if n in hashTable:
            hashTable[n] += 1
        else:
            hashTable[n] = 1

    for key in hashTable:
        freq[hashTable[key]].append(key)
    freq2 = [val for val in freq if val != []]
    res = []

    for i in range(len(freq2) - 1, -1, -1):

        res.extend(freq2[i])

        if len(res) == k:
            return res


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
