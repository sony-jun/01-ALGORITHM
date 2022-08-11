import sys 
sys.stdin = open('input2.txt')

list_ = []
for i in range(1,6):
    name = input()
    if "FBI" in name:
        list_.append(i) # name을 넣으면 첩보명이 나오지만, i를 넣으면 숫자가 나옴

if list_:
    print(*list_)
else:
    print("HE GOT AWAY!")
        

