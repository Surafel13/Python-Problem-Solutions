def MoveNegetiveNumbers(ls):
    left = 0

    for i in range(len(ls)):
        if ls[i] < 0:
            ls[left], ls[i] = ls[i], ls[left]
            left += 1
    
    return ls

print(MoveNegetiveNumbers([3, -1, 0, -4, 8, -2]))