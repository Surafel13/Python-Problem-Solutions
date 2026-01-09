# Computing perifix sum array
#----------------------------

def PerifixSum(ls):
    prefix = [0] * len(ls)
    prefix[0] = ls[0]

    for i in range(len(ls)):
        prefix[i] = prefix[i-1] + ls[i]

    return prefix

def RangeSum(ls, initialI, finallI):
    prefix = PerifixSum(ls)

    if initialI > finallI or finallI > len(prefix):
        return
    rangeSum = prefix[finallI] - prefix[initialI - 1]
    return rangeSum

num4 = [2, 1, 5, 1, 3, 2, 7]

print(RangeSum(num4, 1,3))