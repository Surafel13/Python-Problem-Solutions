# Anagram Implementation

def Anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    hash1 = {}
    for ch in str1:
        if not ch in hash1:
            hash1[ch] = 1
        else:
            hash1[ch] += 1

    for ch in str2:
        if not ch in hash1:
            return False
        hash1[ch] -= 1
        if hash1[ch] < 0 :
            return False
    
    return True



s = "anagram"
t = "nagaram"

print(Anagram(s, t))