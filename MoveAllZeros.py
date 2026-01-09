# Move all 0s to the end
# --------------------

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