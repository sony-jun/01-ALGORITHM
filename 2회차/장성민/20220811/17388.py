import sys
sys.stdin = open('17388.txt')

# 숭실대, 고려대, 한양대 참여도 개수
S, K, H = map(int, input().split())

# 점수-학교 딕셔너리 사용
first = {S: 'Soongsil', K: 'Korea ', H: 'Hanyang'}

if S + K + H >= 100:
    print('OK')
# 가장 작은 참여도 값 찾기
else:
    print(first[min(S, K, H)])