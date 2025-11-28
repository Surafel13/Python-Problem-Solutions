def RemoveElement(self, ls, val):
    
    if len(ls) > 100 or val > 100:
        return

    left = 0
    for right in range(len(ls)):
        if ls[right] > 50 or ls[right] < 0:
            return
        if ls[right] != val:
            ls[left] = ls[right]
            left += 1

    for i in range(left, len(ls)):
        ls[i] = '_'
    count = 0
    for i in ls:
        if i != '_':
            count += 1
    return count

nums = [127]
val = 89
print(RemoveElement(nums, val))