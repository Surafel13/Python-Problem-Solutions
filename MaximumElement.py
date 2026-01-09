#Finding the maximum element of array.
#----------------------------------
def Max(x):
    num = x[0]
    for i in range(len(x)):
        if x[i] > num:
            num = x[i]
        
    print("The maximum number from the list is : " , num)


nums = [3, 1, 8, 2, 5, 1]
Max(nums)