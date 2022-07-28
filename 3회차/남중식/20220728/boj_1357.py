from gzip import READ


X, Y = map(int, input().split())

def Rev(num):
    str_num = str(num)
    return int(str_num[::-1])

print(Rev(Rev(X)+Rev(Y)))