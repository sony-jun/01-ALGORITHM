# https://www.acmicpc.net/problem/2511

from glob import escape


A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))


def card_game(a, b):
    A_point = 0
    B_point = 0
    A_fin = 0
    B_fin = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            A_point +=3
            A_fin = i
        elif b[i] > a[i]:
            B_point +=3
            B_fin = i
        else:
            A_point +=1
            B_point +=1
    print(A_point, B_point)
    if A_point == B_point:
        if a == b:
          print('D')
        elif A_fin > B_fin:
            print('A')
        else:
            print('B')

    elif A_point > B_point:
        print('A')
    else:
        print('B')

card_game(A_list, B_list)

