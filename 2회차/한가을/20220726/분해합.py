# 자연수 N이 있을 때 그 자연수 N의 분해합은
# N과 N을 이루는 각 자리수의 합을 의미
# 어떤 자연수 M의 분해합이 N인 경우
# M을 N의 생성자라 한다.

# 예 : 245의 분해합은 256(=245 + 2 + 4 + 5)
# 따라서 245는 256의 생성자
# 어떤 자연수의 경우 생성자가 없을 수도 있고
# 생성자가 여러 개인 자연수도 있다
# 자연수 N이 주어졌을 때 N의 가장 작은 생성자를 구해 출력

# 첫째 줄에 답을 출력. 생성자가 없으면 0 출력

number = int(input())
result = 0

for i in range(1, number + 1):
    # str 함수를 통해 i의 각 자리수를 리스트 N에 넣음
    N = list(map(int, str(i)))
    # 값 i와 각 자리수가 들어간 리스트 N의 합을 더함
    result = i + sum(N)
    # 합을 더한 것과 number 비교
    if result == number:
        print(i)
        break
    if i == number:
        print(0)