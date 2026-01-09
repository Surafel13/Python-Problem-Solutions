def isThree(num):

    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count >= 3:
        return True
    return False

print(isThree(12))