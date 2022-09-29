import sys
sys.stdin = open('2857.txt')

result = []
# 문자열 5개 입력 받기
for i in range(1, 6):
    # 조건 맞으면 리스트에 해당 번째 할당
    if 'FBI' in input():
        result.append(str(i))

# 저장한것들 하나의 문자열로 join
if len(result) != 0:
    print(' '.join(result))

else:
    print('HE GOT AWAY!')