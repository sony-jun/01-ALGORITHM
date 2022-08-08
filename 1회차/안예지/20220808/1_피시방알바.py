# 1453.
""" 
3
1 2 3


"""
N = int(input())
want = list(map(int, input().split()))
# print(want)

# 중복이 아닌 숫자 모음만 저장할 변수
number = set(want)

# 숫자모음 길이만 빼고 남은 길이는 중복의 갯수
no = len(want) - len(number)
print(no)