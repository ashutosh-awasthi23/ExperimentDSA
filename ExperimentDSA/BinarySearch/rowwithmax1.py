def bs(a):
    lb = len(a)
    start = 0
    end = len(a)-1
    while start<=end:
        mid = (start+end)//2
        if a[mid] == 1:
            lb = mid
            end = mid - 1
        else:
            start = mid + 1
    return len(a) - lb

a = [[0,1,1,1],[1,1,1,1],[0,1,1,1],[0,0,0,0]]
maxi = 0 
for i in a:
    maxi = max(bs(i),maxi) 
print(maxi)
