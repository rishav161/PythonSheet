n=5
for i in range(n,0,-2):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()