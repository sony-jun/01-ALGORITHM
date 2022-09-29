import sys
sys.stdin = open("02_자료구조는_정말최고야.txt", 'r')
'''
N = [*list(map(int, input().split()))]

res = []
ref = True

for _ in range(N[1]):
    if ref == True:
        K = int(input())
        books = [*map(int, input().split())]
        
        for _ in range(len(books)):
            res.append(books.pop())
            if len(books) == 0:
                break
            elif res[-1] < books[-1]:
                continue
            else:
                print("No")
                ref = False
                break
if ref:
    print("Yes")
'''
'''
ref = True

for pile in books:
    if len(res) == 0:
        if sum(pile) == 1 or pile[-1] == 1:
            res.append(pile.pop())
            if len(pile) == 0:
                    break
            elif len(books) == 1:
                res.append(pile.pop())
    else:
        while len(books) != 0 and ref is True:
            ref = False
            for pile in books:
                if pile[-1] == res[-1] + 1:
                    res.append(pile.pop())
                    ref = True
                    if len(pile) == 0:
                        books.remove(pile)

if len(res) == N[0]:
    print("Yes")
else:
    print("No")
'''
N = [*map(int, sys.stdin.readline().split())]

res = []
ref = True

for _ in range(N[1]):
    if ref == True:
        K = int(sys.stdin.readline())
        books = [*map(int, sys.stdin.readline().split())]
        
        while len(books) > 1:
            res.append(books.pop())
            if res[-1] > books[-1]:
                print("No")
                ref = False
                break
if ref:
    print("Yes")