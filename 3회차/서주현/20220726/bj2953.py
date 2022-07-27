import sys

# f = open('bj2953.txt', 'r')
# print(f.readlines())

sys.stdin = open("bj2953.txt", 'r')

scorelist = {}                    # 결과값이 두 개이므로 딕셔너리를 써봄. 
for i in range(1, 6) :            # 인풋은 5개. 
    score = list(map(int, input().split()))
    scorelist[sum(score)]= i       # 총 점수는 딕셔너리의 key로 , 순서는 value로 넣음. 
    
max_ = max(list(scorelist.keys()))   # 총 점수를 비교하고, 해당 점수를 max_ 에 할당. 
print(scorelist[max_], max_)        # max_ 값을 활용해서, 참가자의 순번도 출력
