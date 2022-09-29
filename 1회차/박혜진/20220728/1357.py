def Rev(num) :
    num = str(num)[::-1]

    return int(num)

x, y = input().split()

print(Rev(Rev(x) + Rev(y)))