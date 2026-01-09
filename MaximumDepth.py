def MaximumDepth(st):

    depth = 0
    maxDepth = depth


    for ch in st:
        if ch == "(":
            depth += 1
            maxDepth = max(maxDepth, depth)
        elif ch == ")":
            depth -= 1
        else: continue
    
    return maxDepth


s = "()(())((()()))"
print(MaximumDepth(s))