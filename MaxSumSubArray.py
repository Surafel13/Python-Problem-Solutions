# Finding maximum sum of sub array using window sliding
#------------------------------------------------------

def MaxSumSubarray(nums, k):

    windowSum = sum(nums[:k])
    maxSum = windowSum

    left = 0
    for right in range(k, len(nums)):
        windowSum += nums[right]
        windowSum -= nums[left]
        left += 1

        maxSum = max(maxSum, windowSum)

    return maxSum

num4 = [2, 1, 5, 1, 3, 2, 7]
k = 2

print(MaxSumSubarray(num4, k))