# Return the element that occurs only once in the provided list
a=[1,2,3,4,3,2,1,4,5]
for i in a:
    if(a.count(i)==1):
        print(i)
