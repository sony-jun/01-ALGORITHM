## :sparkler:느낀점/배운점/부족한점



#### BOJ11286 

```python
# heapq 모듈 불러옴
import heapq

numbers = [18, 1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]
# heap 빈 리스트 만듬
heap = []

# numbers에 모든 number 순회
for number in numbers:
    # number가 0이 아니면
    if number != 0:
        # heappush 통해서 numbers의 number 넣음
        heapq.heappush(numbers, number)
    else:
        # length가 정수면
        if len(heap):
            print(0)
        else: # 아니면
            # heappop 통해서 빼낸 numbers 출력
            print(heapq.heappop(numbers))
```



#### BOJ 5063

```python
# 주어진 테스트 케이스를 받음 
tc = int(input())

# 테스트 케이스의 range 처음부터 끝까지 돌음
for _ in range(tc) :
    # map함수 통해서 쪼개고 int로 형변환
    r, e, c = map(int, input().split())
    # (광고를 했을 때 수익 - 광고 비용)이 광고를 하지 않았을 때 수익보다 크면
    if e - c > r :
        # 광고 해야함 출력
        print("advertise")
    # 같으면 
    elif e - c == r :
        # 수익 차이 없음 출력
        print("does not matter")
    # 광고를 하지 않았을 때 수익보다 작으면
    else :
        # 하지 않아야함 출력
        print("do not advertise")
```



#### BOJ 2750

```python
# 주어진 N개의 수 받음
N = int(input())
# 빈 리스트 만듬
num_list = []
# N의 range를 처음부터 끝까지 돌아서 index 꺼냄
for i in range(N):
    # int로 형변환 한 N을 num_list에 추가
    num_list.append(int(input()))
# num_list sort해서 정렬
num_list.sort()
# num_list에 있는 j를 처음부터 끝까지 돌아서 꺼냄
for j in num_list:
    # j 출력
    print(j)
```



#### PRG 숫자문자열

```python
# solution 정의
def solution(s):
    answer = ''
    dic = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'
    }

    answer = s
    # dic의 아이템에 있는 키와 값을 처음부터 끝까지 돌아서 꺼냄
    for key, value in dic.items():
        # answer의 키에 맞는 값을 대체함
        answer = answer.replace(key, value)
    # answer에 int 형변환해서 반환
    return int(answer)


# Programmers 다른 사람의 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
```



:sparkles::rocket: 자연수를 넣고 빼는 과정을 heap의 heappush와 heappop를 사용하여 문제풀이 연습을 했는데 수업에서 배운 과정을 이해할 수 있어서 좋았고 기초 문제는 map함수, sort 메서드, dictionary 등을 활용할 수 있어서 부족한 부분을 채우는 연습이 되었습니다. 