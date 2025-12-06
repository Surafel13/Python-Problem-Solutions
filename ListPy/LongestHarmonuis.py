def LongestHarmoniousArray(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    longest = 0

    for x in freq:
        if x + 1 in freq:
            longest = max(longest, freq[x] + freq[x + 1])

    return longest



nums0 = [1,3,2,2,5,2,3,7]
print(LongestHarmoniousArray(nums0))