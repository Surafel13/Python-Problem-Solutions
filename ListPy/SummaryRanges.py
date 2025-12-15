def summaryRanges(nums):
    output = []

    left = 0
    for i, num in enumerate(nums):
        if num + 1 in nums:
            continue
        if nums[left] == num:
            output.append("{}".format( num))
            left = i + 1
            continue
        output.append("{}->{}".format(nums[left], num))
        left = i + 1

    return output


nums = [0,2,3,4,6,8,9]
print(summaryRanges(nums))