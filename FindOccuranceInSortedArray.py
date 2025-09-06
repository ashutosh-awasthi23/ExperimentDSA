a
def first_occurance(a,target):
    start = 0
    end = len(a)-1
    while start<=end:
        mid = (start+end)//2
        if a[mid] == target:
            result = mid
            end = mid-1
        elif a[mid] < target :
            start = mid + 1
        else:
            end = mid - 1
    return result

def last_occurance(a,target):
    start = 0
    end = len(a)-1
    while start<=end:
        mid = (start+end)//2
        if a[mid] == target:
            result = mid
            start = mid + 1
        elif a[mid] < target :
            start = mid + 1
        else:
            end = mid - 1
    return result

a = [1,1,2,2,2,2,2,3,3,3]
target = 2 
print(last_occurance(a,target)-first_occurance(a,target)+1)