def majorityElement(nums):
    lenNum = len(nums) / 2
    hsh = {}

    for num in nums:
        hsh[num] = hsh.get(num, 0) + 1
    
    for i in hsh:
        if hsh[i] > lenNum:
            return i
    
    return None

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
