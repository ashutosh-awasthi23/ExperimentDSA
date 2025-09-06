a = [2,3,4,5,6,7,8,9,10,0,1]
def bs(a):
    start = 0
    end = len(a) - 1
    while start<end:
        mid = (start+end)//2
        if a[mid] > a[end]:
            start = mid+1
        else:
            end = mid
    return a[start]

print(bs(a))