def MaximumAverageSubarray(ls, k):
    total = sum(ls[:k])
    windowAverage = total / k
    maximumAverage = windowAverage
    left = 0

    for i in range(k, len(ls)):
        total = total - ls[left] + ls[i]
        left += 1
        maximumAverage = max(maximumAverage, windowAverage)

    return maximumAverage

nums = [1,12,-5,-6,50,3]
k = 4
print(MaximumAverageSubarray(nums, k))