# 시작번호는 3,4,5,6,9
# - 포함가능, -제외 16자리
# 만들수 있으면 1, 없으면 0
T = int(input())
for test_case in range(1,T+1):
    numbers = input()
    result = 1
    if numbers[0] not in '34569':
        result = 0
    numbers = numbers.replace('-','')
    if len(numbers) != 16:
        # print(len(numbers))
        result = 0
    print(f'#{test_case}',result)
