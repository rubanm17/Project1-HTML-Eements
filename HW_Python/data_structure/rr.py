def myfunction1(n):
    if(n>0):
        return
    for i in range (0,n+1):
        print("codingal")
    myfunction1(n/2)
    myfunction1(n/3)
print(myfunction1(10))
def myfunction2(n):
    if(n<=1):
        return
    print("codingal")
    myfunction2(n-1)
print(myfunction2(10))