def prints(n):
    if(n<=0):
        return
    print("Codingal")
    prints(n/2)
    prints(n/2)

#text
#t(n) = t(n/2) + t(n/2) for 2 recursive calls and for rest code our function will take constant time.   
#so, our reccurence relation will be:
#(n) = t(n/2) + t(n/2)+0(1) when n>0
#the reccurence tree for t(n) = t(n/2) + t(n/2) +0(1) will be:
#            t(n)
#            /      \
#        t(n/2)     t(n/2)
#        /   \        /    \
#   t(n/4) t(n/4)  t(n/4) t(n/4)        