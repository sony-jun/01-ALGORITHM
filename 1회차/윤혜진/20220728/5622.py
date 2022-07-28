# https://www.acmicpc.net/problem/5622
# 문제5622번.다이얼
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 알파벳 대문자로 이루어진 단어 1개
- 2 <= 단어의 길이 <= 15
'''



# 출력
'''
1. 다이얼을 걸기 위해서 필요한 최소 시간
- 전화번호 = 각 숫자에 해당하는 문자
- 숫자 1을 걸려면 총 2초 필요
- 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸림
'''



# 코드
import sys

sys.stdin = open('input_text/5622.txt')

word = input()

# 키=알파벳, 값=번호인 딕셔너리 생성
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '22233344455566677778889999'
alp_num = dict(zip(alphabet, number))
print(alp_num)

# 문자의 각 알파벳에 해당하는 번호 찾고, 시간 더하기
tot_time = 0
for char in word:
    # 번호 0일때는, 돌리는 시간 = 11초 
    if alp_num[char] == '0':
        tot_time += 11
        continue
    # 번호 1 ~ 9일때, 돌리는 시간 = 자신의 번호 + 1
    tot_time += int(alp_num[char]) + 1

print(tot_time)



# 실행결과(메모리:30840KB, 시간:68ms)