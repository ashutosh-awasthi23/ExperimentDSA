n =  10
def factorialFun(n):
    if n <=1:
        return n
    return (factorialFun(n-1)*n)

factorialFun(10)

def sum(n):
    if n ==1 :
        return 1
    return (sum(n-1)+n)
print(sum(n))