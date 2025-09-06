def searchInsert(nums,target):
    start = 0
    end = len(nums)-1
    while start <= end :
        mid = (start+end)//2
        if nums[mid]==target:
            return mid

        elif nums[mid]<target:
            start = mid+1
        else: 
            end = mid-1
    return start
a =[1,3,4,5,6,7,8,9,20]
print(searchInsert(a,21))