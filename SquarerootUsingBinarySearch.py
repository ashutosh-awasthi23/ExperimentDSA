def sr(n):
    start = 1 
    end = 10
    res = -1
    while start<=end:
        mid = (start+end)//2
        if mid * mid > n:
            end = mid -1
        else:
            res = mid
            start = mid + 1
    return res
print(sr(99))