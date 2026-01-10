class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        res = "-" if numerator * denominator < 0 else ""
        n, d = abs(numerator), abs(denominator)
        res += str(n // d)
        n %= d
        if n == 0:
            return res
        res += "."
        seen = {}
        while n:
            if n in seen:
                i = seen[n]
                res = res[:i] + "(" + res[i:] + ")"
                break
            seen[n] = len(res)
            n *= 10
            res += str(n // d)
            n %= d
        return res
