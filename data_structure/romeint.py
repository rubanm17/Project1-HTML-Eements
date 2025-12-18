def romanToInt(romanInput):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    resultInteger = 0

    for i in range(0,len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger += roman[romanInput[i]]
    resultInteger += roman[romanInput[-1]]
    return resultInteger
romanInput = input("enter the roman numeral")
print("integer equilavent:", romanToInt(romanInput))