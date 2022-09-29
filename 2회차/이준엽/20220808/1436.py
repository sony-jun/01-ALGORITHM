# 666 1666 2666 3666 4666 5666 
# (6660 6661 6662 6663 6664 6665 6666 6667 6668 6669)
# 7666 8666 9666

# 10666 11666 12666 13666 14666 15666
# (16660 16661 16662 16663 16664 16665 16666 16667 16668 16669)
# 17666 18666 19666

# 20

# 30

# 40

# 50

# 60666 61666 62666 63666 64666 65666
# (66600 ~ 66699)
# # 67666 68666 69666
from xml.etree.ElementTree import TreeBuilder


cnt = 0
n = int(input())
for i in range(666*10000000):
    if '666' in str(i):
        cnt+=1
        if cnt==n:
            print(i)
            break

n = int(input())
nth = 666
cnt = 0
while True:
    if '666' in str(nth):
        cnt+=1
    if cnt == n:
        print(nth)
        break
    nth+=1


n = int(input())
nth = 666
cnt = 0 
while True:
    if '666' in str(nth):
        cnt+=1
    if cnt == n:
        print(nth)
        break
    nth+=1