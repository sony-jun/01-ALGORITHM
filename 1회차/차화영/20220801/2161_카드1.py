import sys
sys.stdin = open("2161.txt")

T = int(input())
num = []
remove_num = [] # 버리는 카드
for n in range(1, T+1):
    num.append(n)
while len(num) != 1: # num의 길이가 1이 아니면 계속 실행
    remove_num.append(num.pop(0)) # pop - 인덱스가 0인 요소를 삭제하고, remove_num에 삭제한 값들을 추가한다.
    num.append(num.pop(0)) # pop - 가장 위에 있는 숫자를 꺼내서 num에 추가하면 가장 마지막으로 온다.
for i in remove_num:
    print(i, end=' ') # 버리는 카드들 ; remove_num을 순서대로 출력
print(num[0]) # while문이 다 순회 후 남게 되는 카드 출력