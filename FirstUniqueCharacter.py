# The first unique letter from a string that has no repetition.
# ------------------------------------------------------------
def UniqueChracter(st):
    hash = {}

    for i, char in enumerate(st):
        if not char in hash:
            hash[char] = 1
        else:
            hash[char] += 1
    for i, stl in enumerate(hash):
        if hash[stl] == 1:
            return i

    return -1


s = "loveleetcode"
print(UniqueChracter(s))