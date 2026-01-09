# Reversing array using tow pointer.
#----------------------------------
def ReveseArray(nums):
    left = 0
    right = len(nums) - 1

    while left < right :
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

nums = [3, 1, 8, 2, 5, 1]
print(ReveseArray(nums))