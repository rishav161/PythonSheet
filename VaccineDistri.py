import math
t=int(input())
for i in range(t):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    ri=0
    nri=0
    for j in range(n):
        if a[j]>=80 or a[j]<=9:
            ri+=1
        else:
            nri+=1
    print(math.ceil(ri/d)+math.ceil(nri/d))