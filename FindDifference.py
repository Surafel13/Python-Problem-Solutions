def findTheDifference(st1, st2):
    for i in st2:
        if not i in st1:
            return i
        elif i in st1 and st1.count(i) != st2.count(i):
            return i

print(findTheDifference("a", "aa"))
        