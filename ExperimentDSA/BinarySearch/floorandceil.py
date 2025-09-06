def floor(a,target):
    start = 0 
    end = len(a)
    while start < end:
        mid = (start+end)//2
        if a[mid] <= target:
            lb = a[mid]
            start = mid +1
        else:
            end = mid-1
    return lb
def ceil(a,target):
    start = 0 
    end = len(a)
    while start < end:
        mid = (start+end)//2
        if a[mid] <= target:
            start = mid +1
        else:
            ub = a[mid]
            end = mid-1
    return ub