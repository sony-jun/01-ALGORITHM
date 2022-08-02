# 테스트 케이스의 수를 입력
test_case = int(input())

# 각 테스트 케이스마다 값을 입력받아 data 리스트에 저장
for i in range(test_case) :
    data = list(map(int, input().split()))
    result = 0 # 남은 한변의 값
    # data 중 첫번째에 들어있는 값이 3개일경우 남은 1변의 길이도 이와 같다
    if data.count(data[0]) == 3 :
        result = data[0]
    else :
        # data 중 가장 큰 값이 1개일때 남은 1변의 길이가 이와 같다.
        if data.count(max(data)) == 1 :
            result = max(data)
        # data 중 가장 큰 값이 1개가 아니면, 남은 1변의 길이는 최소값과 같다.
        else :
            result = min(data)
    print('#%d %d' % (i+1, result))