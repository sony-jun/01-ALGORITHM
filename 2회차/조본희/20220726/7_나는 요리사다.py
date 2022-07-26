import sys

sys.stdin = open("7_input.txt")
cooks = []

for i in range(5):
    #입력받은 동시에 총점수 저장
    cooks.append(sum(map(int, input().split())))
#index+1로 참가자번호, 해당참가자 점수 출력
print(cooks.index(max(cooks))+1, max(cooks))