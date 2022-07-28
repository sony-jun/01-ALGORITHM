x,y = input().split()
def Rev(x):
    x = ''.join(reversed(str(x)))
    x = int(x)
    return x
print(Rev(Rev(int(x))+Rev(int(y))))