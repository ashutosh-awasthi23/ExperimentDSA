def bs(li,target):
    start = 0
    end  = len(li)-1
    while start<=end:
        mid = (start+end)//2
        if li[mid] == target:
            return li[mid]
        elif li[mid] > target:
            ans = li[mid]
            end = mid-1
        else:
            start = mid+1
    return ans


def bs2(li,target):
    start = 0
    end  = len(li)-1
    while start<=end:
        mid = (start+end)//2
        if li[mid] == target:
            return li[mid]
        elif li[mid] < target:
            ans = li[mid]
            start = mid+1
        else:
            end = mid - 1
    return ans

li = [12,13,56,78,90,123,247,1000]
target = 57

print(bs(li,target))
print(bs2(li,target))