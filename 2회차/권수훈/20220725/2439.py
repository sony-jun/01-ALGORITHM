starNumber = int(input())

for i in range(1,starNumber+1):
    print(" "*(starNumber-i), end="")
    print("*"*i)