def bs(m,n):
    start = 1
    end = m
    while start<=end:
        mid = (start+end)//2
        if mid**n == m:
            return mid
        elif mid**n  > m:
            end = mid -1
        else :
            start = mid + 1
    return -1

print(bs(28,3))