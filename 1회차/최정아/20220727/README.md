## :sparkler:느낀점/배운점/부족한점



#### BOJ 1157 단어 공부

```python
text = input()

# 대문자로 바꿔서 저장
value = text.upper()
# set() 함수로 중복된 값 제거하고 문자열 집합을 담음
values = list(set(value))

maxcount = 0

# for문으로 values(M,I,S,P)가
for i in range(len(values)):
    # value에 몇 개 있는지 확인
    cnt = value.count(values[i])
    # 값이 최대값이면
    if cnt == maxcount:
        # maxcount에 저장
        maxcount = cnt
        # 최대값이 여러 개 존재하면 ? 출력 조건 
        maxchar = '?' 
        
        # 예시) values(M,I,S,P)의 values[i] = values[0] = M
        # value.count(values[i]) = M의 개수 1, 그래서 cnt = 1

    elif cnt > maxcount:
        # values[0] = M 이면 cnt = 1
        maxcount = cnt # 1
        maxchar = values[i] # M
    else:
        pass

print(maxchar.upper())
```



#### BOJ 2851 슈퍼마리오

```python
def solution():
    answer = 0
    for _ in range(10):
        # 버섯 점수 확인
        score = int(input())
        # 버섯 점수 증가 
        answer += score
        # answer이 100 이상이면
        if answer >= 100:
            # (answer - score) = prev 
            prev, nxt = 100 - (answer - score), abs(answer - 100)
            if prev < nxt:
                answer -= score
                return answer
            elif nxt < prev or prev == nxt:
                return answer
    return answer

print(solution())

```



#### BOJ 7568 덩치

```python
n = int(input())

data = [] # 입력된 정보 저장 리스트
ans = [] # 등수정보 저장 리스트
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b)) # 키와 몸무게 추가

for i in range(n):
    count = 0
    for j in range(n):
        # 자신보다 몸무게와 키가 큰 사람 수 확인
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    ans.append(count + 1)

for d in ans:
    print(d,end=" ")
```



:sparkles::rocket: for문 안에 조건문 확장을 연습했고 다양한 문법을 자유롭게 사용할 수 있게 되는 날이 기다려집니다. 