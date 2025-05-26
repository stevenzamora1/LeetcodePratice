def dailyTemperatures(temperatures: list[int]) -> list[int]:
    arr = [0] * len(temperatures)
    tempStack = [0]

    for i in range(1, len(temperatures)):
        if temperatures(tempStack[-1]) < temperatures[i]:
            arr[i] = i - tempStack[-1]

    return arr


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
