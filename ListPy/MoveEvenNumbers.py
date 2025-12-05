def MoveEvenNumbersToBeginning(ls):
    
    left = 0
    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            ls[left], ls[i] = ls[i], ls[left]
            left += 1
    return ls







nums = [3,1,2,4]
print(MoveEvenNumbersToBeginning(nums))