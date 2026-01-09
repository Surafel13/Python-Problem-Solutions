def removeDigit(st, num):
    numArray = []

    for i in range(len(st)):
        if st[i] == num:
            news = st[:i] + st[i+1:]
            numArray.append(news)


    return max(numArray)

number = "551"
digit = "5"
print(removeDigit(number, digit))