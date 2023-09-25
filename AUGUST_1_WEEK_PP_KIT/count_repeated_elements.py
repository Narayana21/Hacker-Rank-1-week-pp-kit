# return the array of repeated elements

a=[1,12,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,12,23]
l=len(a)
print(l)
freq=[]
for i in range(l):
    freq.append(a.count(a[i]))
print(freq)

f=[0]*l
for i in range(l):
    f[i]=a.count(a[i])
print(f)