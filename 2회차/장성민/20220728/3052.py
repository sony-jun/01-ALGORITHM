# 서로 다른 나머지 개수를 위한 리스트 생성
li = []

# 10개의 입력을 위한 반복, 나머지 할당
for i in range(10):
    num = int(input())
    li.append(num % 42)

# 중복값 제거를 위해 set 활용
set_ = set(li)
print(len(set_))