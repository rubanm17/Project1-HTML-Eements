def sum(n):
    return n*(n+1)/2

# space complexity : 0(1) ,auxilary space:0(1)
#linear space
def arraysum(a):
    sum=0
    for i in a:
        sum=sum+i
    
    return(sum)

a=[12,3,4,15]
arraysum(a)

# with size of an array , the space also required increase
# space  complexity :0(1),auxilary space:0(1)
def summ(n):
    if (n<+0):
        return
    return n+ summ(n-1)

# 10
# ^
# |
# sum(4) <\
# ^        | +6 
# |       /
# sum(3)  <\
# ^         | +3
# |        /
# sum(2) <\
# ^        | +1
# |       /
# sum(1)  <\
# ^         | +0
# |        /
# sum(0)</