# https://www.acmicpc.net/problem/2577

# A, B, C 세개의 입력을 받음
A = int(input())
B = int(input())
C = int(input())

# 세 수를 곱한뒤, 문자열로 사용하기 위해 str로 형변환
result = A * B * C
result = str(result)

# 0~9까지 넣을 수 있는 딕셔너리를 만듦.
num_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

# 만약 num가 num_dict에 있는 key와 일치하면
for num in result:
    if num in num_dict.keys():
        # num_dict의 value를 +1
        num_dict[num] += 1

# 딕셔너리의 value들을 출력
for num in num_dict:
    print(num_dict[num])
