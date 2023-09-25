# array size will be dynamic
# fllipping matrix
arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n= len(arr)
n2=n//2
sum=0
for i in range(n2):
    for j in range(n2):
        sum+=max(arr[i][j],arr[i][n-j-1],arr[n-i-1][j],arr[n-i-1][n-j-1])
print(sum)