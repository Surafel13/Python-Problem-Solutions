def minLength(st):

    stack = []
    for ch in st:
        if  stack:
            if ch == "B" and stack[-1] == "A":
                stack.pop()
            elif ch == "D" and stack[-1] == "C":
                stack.pop()
            else :
                stack.append(ch)
        else:
            stack.append(ch)
    
    return len(stack)

s = "ACBBD"
print(minLength(s))

        
            