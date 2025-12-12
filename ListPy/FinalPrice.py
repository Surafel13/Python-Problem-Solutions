def finalPrices(ls):   
    discount = ls[:]

    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            if discount[i] >= discount[j]:
                discount[i] -= discount[j]
                break

    return discount



prices = [8,4,6,2,3]
print(finalPrices(prices))