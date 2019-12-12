#coding:utf-8
result=[]
m=input('please enter m: ')
if (m%6!=2 and m%6!=3):
    if m%2==0:
        for i in range(2,m+1,2):
            result.append(i)
        for i in range(1,m,2):
            result.append(i)
    else:
        for i in range(2,m,2):
            result.append(i)
        for i in range(1,m-1,2):
            result.append(i)
        result.append(m)
else:
    n=m//2
    if (m%2==0 and n%2==0):
        for i in range(n,m+1,2):
            result.append(i)
        for i in range(2,n-1,2):
            result.append(i)
        for i in range(n+3,m,2):
            result.append(i)
        for i in range(1,n+2,2):
            result.append(i)
    elif (m%2==0 and n%2!=0):
        for i in range(n, m , 2):
            result.append(i)
        for i in range(1, n+3, 2):
            result.append(i)
        for i in range(n+3, m + 1, 2):
            result.append(i)
        for i in range(2, n + 2, 2):
            result.append(i)
    elif (m%2!=0 and n%2==0):
        for i in range(n, m , 2):
            result.append(i)
        for i in range(2, n-1, 2):
            result.append(i)
        for i in range(n+3, m -1, 2):
            result.append(i)
        for i in range(1, n + 2, 2):
            result.append(i)
        result.append(m)
    else:
        for i in range(n, m - 1, 2):
            result.append(i)
        for i in range(1, n-1, 2):
            result.append(i)
        for i in range(n+3, m, 2):
            result.append(i)
        for i in range(2, n + 2, 2):
            result.append(i)
        result.append(m)

for i in range(1,m+1):
    for j in range(1,m+1):
        if j==result[i]:
            print'Q',
        else:
            print'-',
    print
