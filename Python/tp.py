#empty List

mt = ()

# Tuple having integers
mt = (1,2,3)
print(mt)

#Tuple with mixed datatypes
mt = (1,"Hello",3,4)
print(mt)

#nested tuple
mt = ("mouse",[5,6,7,8],[9,10,11,12])
print(mt)

#accessing tuple elementss using indexing
mt = ('p','e','r','m','i','t')
print(mt[0])
print(mt[5])

#nested tuple
ntp = ("mouse",[8,9,0],[1,2,3,4,5,6,7])

#nested index
print(ntp[0][3])
print(ntp[1][1])
#slicing
print("Sliced:", mt[1:4])

#literating through tuple
for letter in (mt):
    print("Hello", letter)