# Pair sum in sorted array
def PairSum(ls, target):
    result = []

    left = 0
    right = len(ls) - 1
    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return[]

nums = [1, 2, 3, 4, 6]
target = 6
print(PairSum(nums, target))