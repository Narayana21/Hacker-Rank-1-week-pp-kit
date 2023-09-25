# s='This day is so good'
# dict={}
# for i in s:
#    dict[i]=s.count(i)
# print(dict)

a=[[1,25,34],[4,57,89],[47,85,90]]
c=-1
k1=0
for i in range(len(a)):
    for j in range(len(a[0])):
        c=c+1
        c1=c
        for k in range(len(a)):
            for l in range(len(a[0])):
                if c1!=0:
                    c1=c1-1
                    continue
                if a[i][j]>a[k][l]:
                    a[i][j],a[k][l]=a[k][l],a[i][j]
print(a)