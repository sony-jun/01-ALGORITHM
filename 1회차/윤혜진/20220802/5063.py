# https://www.acmicpc.net/problem/5063
# 문제5063번.TGN
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 테스트 케이스 T
2. 3개의 정수 r, e, c
- r: 광고를 하지 않았을 때 수익
- e: 광고를 했을 때의 수익
- c: 광고 비용
- -1,000,000 <= r,e <= 1,000,000
- 0 <= c <= 1,000,000
'''



# 출력
'''
1. 광고를 해야한다면 'advertise', 하지 않아야 한다면 'do not advertise', 광고를 해도 수익 차이가 없다면 'does not matter'
'''



# 코드
import sys

sys.stdin = open('input_text/5063.txt')

T = int(input())
for _ in range(T):
    r, e, c = map(int, input().split())

    # 광고를 하는 경우 발생하는 수익
    do_ad = e - c

    # 광고 여부에 따른 수익 비교
    if do_ad > r:
        print('advertise')
    elif do_ad < r:
        print('do not advertise')
    else:
        print('does not matter')



# 실행결과(메모리:30840KB, 시간:76ms)