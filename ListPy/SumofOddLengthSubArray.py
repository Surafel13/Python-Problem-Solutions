def WindowSumSubarray(ls, k):
    window = sum(ls[:k])
    windowSum = window

    left = 0
    for i in range(k, len(ls)):
        window -= ls[left]
        window += ls[i]
        left += 1
        windowSum += window

    return windowSum


def sumOddLengthSubarrays(ls):
    k = 1
    result = 0
    for i in range(len(ls)):
        if k <= len(ls):
            result += WindowSumSubarray(ls, k)
            k += 2

    return result



arr = [10,11,12]
print(sumOddLengthSubarrays(arr))