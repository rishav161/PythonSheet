n=5

for i in range(n,0,-1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")

    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
# lower half
for i in range(2,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")

    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()