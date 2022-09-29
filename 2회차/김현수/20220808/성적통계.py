import sys
sys.stdin = open("성적통계.txt")

T = int(input())

for _ in range(T):

    list_ = list(map(int,input().split()))
    list_.pop(0)
    list_.sort(reverse=True)
    #print(list_)
    larg = list_[0] - list_[1]
    for i in range(len(list_)-1):
        if larg < list_[i] - list_[i+1]:
            larg = list_[i] - list_[i+1]
    print(f'Class {_+1}')
    print(f'Max {max(list_)}, Min {min(list_)}, Largest gap {larg}')