def countGoodTriplets(ls, num1, num2, num3):
    result = []

    for i, numi in enumerate(ls):
        for j , numj in enumerate(ls):
            for k, numk in enumerate(ls):
                if i < j < k:
                    a = abs(ls[i] - ls[j]) 
                    b = abs(ls[j] - ls[k] )
                    c = abs(ls[i] - ls[k])
                    if a <= num1 and b <= num2 and c <= num3:
                        result.append((a, b, c))

    return len(result)


arr = [1,1,2,2,3],
a = 0
b = 0
c = 1
print(countGoodTriplets(arr, a, b, c))