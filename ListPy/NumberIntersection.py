def NumberIntersection(ls1, ls2):
    hash1 = {}

    for i , num in enumerate(ls1):
        if not num in hash1:
            hash1[num] = i
    outPut = []
    for i in ls2:
        if i in hash1:
            if i in outPut:
                continue
            outPut.append(i)
    
    return outPut

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(NumberIntersection(nums1, nums2))