def myfunction(n):
    count = 0
    for i in range(0,n+1):
        print("First Loop")
        count += 1
    print("Count of 1st loop is ", count)
 
    j=1
    count1 = 0
    while(j<=n+1):
        print("Second Loop ",j)
        count1 += 1
        j=j*2
    print("count of 2nd loop is: ", count1)
 
    count2 = 0
    for i in range(0,100):
        print("Third loop")
        count2 += 1
    print("count of 3rd loop is: ", count2)

a = int(input("Enter the number of iteration to be done : "))
myfunction(a)