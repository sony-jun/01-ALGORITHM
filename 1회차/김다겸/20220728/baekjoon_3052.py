a = []
b = []

# input 받은 값을 리스트로 저장
for i in range(10):
    a.append(int(input()))

# 리스트 a를 순회
for i in range(len(a)):
    # 입력 받은 값들을 42로 나눈 나머지 b 리스트에 추가
    b.append(a[i] % 42)

# set로 b의 중복 제거 후 list로 바꾼 후 갯수 구하기
print(len(list(set(b))))