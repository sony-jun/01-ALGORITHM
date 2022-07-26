"""
# 2846.
자전거 길은 오르막길, 내리막길, 평지로 이루어져 있으며,
일정 거리마다 높이를 측정한다.
가장 큰 오르막길의 크기를 구하려고 한다.
측정한 높이는 길이가 N인 수열로 나타낼 수 있다.
여기서 오르막길은 적어도 2개의 수로 이루어진 높이가 증가하는 '부분 수열'이다.
오르막길의 크기는 부분 수열의 첫 번재 숫자와 마지막 숫자의 차이이다.

예를 들어, 높이가 
12 '3 5 7 10' 6 '1 11' 인 길이 있다고 했을 때,
두 개의 오르막길 중 첫 번째 오르막길의 크기는 7(= 10 - 3)이고,
두 번째 오르막길의 크기는 10(= 11 - 1)이다.
높이가 12와 6인 곳은 오르막길에 속하지 않는다.
가장 큰 오르막길을 구하는 프로그램 작성하기

# 입력
첫째 줄에 상근이가 측정한 높이의 수이자 수열의 크기인 N이 주어진다.(수열의 크기)
N(1 <= N <= 1000)
둘째 줄에는 N개의 양의 정수 Pi가 주어진다.(수열)
Pi(1 <= Pi <= 1000)
각 숫자는 상근이가 측정한 높이이다.

# 출력
첫째 줄에 가장 큰 오르막길의 크기를 출력,
오르막길이 없는 경우 0을 출력한다.

# 접근
1. 리스트를 순회하면서(반복 횟수)
2. 현재 값보다 작은 수가 나오면,
3. 리스트를 초기화하고
4. 새로운 리스트에 넣는다.
5. 만들어진 부분 수열에서 리스트별로
6. 맨 처음 인덱스와 맨 끝 인덱스의 값을 연산하여
7. 그 합끼리 비교하여 출력하기


"""
N = int(input())
number_list = list(map(int,input().split()))
# print(number_list)
small_list = []
new_number_list = []
# 부분수열을 담을 리스트
for idx in range(len(number_list)):
    # 리스트를 순회하면서 해당 바인딩된 인덱스 값을 부분수열에 추가합니다.
    small_list.append(number_list[idx])
    if idx + 1 == len(number_list):
        break
    # 직후 인덱스의 값이 number_list의 길이랑 같아지면 반복을 종료합니다.
    if number_list[idx] < number_list[idx + 1]:
        # 직후 인덱스의 값이 현재 바인딩된 인덱스 값보다 크다면
        small_list.append(number_list[idx + 1])
    elif number_list[idx] >= number_list[idx + 1]:
        new_number_list.append(small_list)
        small_list.clear()
        # 그렇지 않다면 부분수열을 초기화합니다.
        
        
print(new_number_list)