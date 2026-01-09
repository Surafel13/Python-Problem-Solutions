def ContainDuplicate(ls, k):
    
    hsh = {}

    for i , num in enumerate(ls):
        if num in hsh and abs(i - hsh[num] <= k):
            return True
        hsh[num] = i
    
    return False
            



nums = [1,2,3,1,2,3]
k = 2
print(ContainDuplicate(nums, k))
