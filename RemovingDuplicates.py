# Removing duplicates from sorted array
#---------------------------------------

def removeDuplicates(nums):
    if not nums:
        return nums
    
    left = 0
    for i in range(len(nums)):
        if nums[left] != nums[i]:
            left += 1
            nums[left] = nums[i]
        
    return nums[:left+1]
nums3 = [1, 1, 2, 2, 3]
print(removeDuplicates(nums3))