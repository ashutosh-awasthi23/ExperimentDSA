def lowerbound(nums,target):
    start = 0 
    end = len(nums)
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid 
    return start

a = [1,2,4,5,6,8,9,11]
print(lowerbound(a,7))