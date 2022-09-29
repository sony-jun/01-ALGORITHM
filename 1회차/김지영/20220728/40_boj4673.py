def d(n):
    sepn = list(map(int,str(n))) # M의 자리수를 구하기 위한 sepM
    return n+sum(sepn)

yesdn = set()

for i in range(1,10001):
    yesdn.add(d(i))

for i in range(1,10001):
    if i not in yesdn:
        print(i)

# # 시간초과아악...