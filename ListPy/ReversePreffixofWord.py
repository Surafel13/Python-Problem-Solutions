def reversePrefix(word, ch):

    stack = []

    for i in range(len(word)):
        if word[i] != ch:
            stack.append(word[i])
        elif word[i] == ch:
            stack.append(word[i])
            wd = word[i + 1:]
            break
        else:
            continue
    stack.reverse()
    return "".join(stack) + wd



print(reversePrefix("abcdefd", "d"))