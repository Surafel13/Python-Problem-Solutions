import math

def CountTriple(num):
    count = 0

    for a in range(1, num+1):
        for b in range(1, num+1):
            c = math.isqrt(a*a + b*b)
            if c <= num and a*a + b*b == c*c:
                count += 1
    
    return count

print(CountTriple(10))