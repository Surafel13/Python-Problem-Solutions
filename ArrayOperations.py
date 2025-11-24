# Finding the maximum element of array.
def Max(x):
    num = x[0]
    for i in range(len(x)):
        if x[i] > num:
            num = x[i]
        
    print("The maximum number from the list is : " , num)


nums = [3, 1, 8, 2, 5, 1]
Max(nums)


# Reversing array using tow pointer.
def ReveseArray(nums):
    left = 0
    right = len(nums) - 1

    while left < right :
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

print(ReveseArray(nums))

# Move all 0s to the end

def MoveAllZerosToEnd(nums) :
    left = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1
        
    for i in range(left, len(nums)):
        nums[i] = 0
    
    return nums

nums2 = [1, 0, 4, 9, 0, 9]
print(MoveAllZerosToEnd(nums2))