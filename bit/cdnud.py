def divide(od,odv):

    sign = (-1 if((od < 0)^(odv < 0))else 1)

    od = abs(od)
    odv = abs(odv)

    qn = 0
    tn = 0

    for i in range(31 , -1, -1):

        if(tn + (od << i) <= odv):
            tn += odv << i
            qn |= 1 << i

    if sign == -1:
        qn = -qn
    return qn

a = int(input("Enter the value a:"))
b = int(input("Enter the value b:"))
print("Result of ",a," / ",b," is: ",divide(a,b))