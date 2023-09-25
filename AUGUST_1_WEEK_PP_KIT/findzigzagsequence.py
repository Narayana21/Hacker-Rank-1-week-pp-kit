# sample ip=[1,2,3,4,5,6,7]
# sample op=[1,2,3,7,6,5,4]

a= [2,1,4,3,7,6,5] # unordered i/p
n=len(a)
a.sort()
mid=n//2
a[mid],a[n-1]=a[n-1]