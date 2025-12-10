def removalDuplicates(st):

    stack = []
    
    for ch in st:
        if not stack or stack[-1] != ch:
            stack.append(ch)
        else:
            stack.pop()

    return "".join(stack)
            
   

    


s = "abbaca"
print(removalDuplicates(s))