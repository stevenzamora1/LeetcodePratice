import math


def minEatingSpeed(piles: list[int], h: int) -> int:

    l, r = 0, max(piles)
    answer = r
    while l <= r:
        halfpoint = (l + r) // 2
        hours = 0
        print(halfpoint)
        for n in piles:
            hours += math.ceil(n / halfpoint)

        if hours <= h:
            answer = min(halfpoint, answer)
            r = halfpoint - 1

        else:

            l = halfpoint + 1

    return answer


print(minEatingSpeed([3, 6, 7, 11], 8))
# print(minEatingSpeed([30, 11, 23, 4, 20], 5))
# print(minEatingSpeed([30, 11, 23, 4, 20], 6))
