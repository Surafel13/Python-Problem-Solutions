def greatestLetter(st):

    result = []
    for i in st:
        upper = i.upper()
        lower = i.lower()

        if upper in st and lower in st:
            if not upper in result:
                result.append(upper)

        else :
            continue
    
    if result:
        return max(result)
    return ""

s = "arRAzFif"
print(greatestLetter(s))
