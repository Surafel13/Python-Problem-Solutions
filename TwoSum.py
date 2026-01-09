# Computing sum that equal with the target and return their indece
# ----------------------------------------------------------------

def TwoSum(ls, target):
    hash = {}

    for i, num in enumerate(ls):
        diff = target - num

        if diff in hash:
            return [hash[diff], i]
        hash[num] = i

    return []

nums = [1, 2, 4, 6, 3, 6, 7]
target = 7
print(TwoSum(nums, target))