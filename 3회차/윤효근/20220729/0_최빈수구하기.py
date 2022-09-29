import collections
import sys

sys.stdin = open("최빈수.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    count = {}                  #딕셔너리 생성
    most = []                   #최빈수 리스트 생성
    case = int(input())         # 테스트 케이스 번호
    scores=list(map(int,input().split()))   #점수 입력 받기
    count.update(collections.Counter(scores))   #입력받은 점수를 딕셔너리로 변환하여 count에 update
    for k,v in count.items():
        if v == max(count.values()):        #value가 가장 높으면 최빈수
            most.append(k)
    print(f'#{case} {max(most)}')

