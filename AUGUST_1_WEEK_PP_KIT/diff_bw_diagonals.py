# Find the absoulte diff bw the two diagainals of matrix

arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
pd=[]
sd=[]
n=len(arr)
for i in range(n):
    for j in range(n):
        if(i==j):
            pd.append(arr[i][j])
        if((i+j)==(n-1)):
            sd.append(arr[i][j])
pds=sum(pd)
sds=sum(sd)
abd=abs(pds-sds)
print(abd)

a=[0]*2
print(a)