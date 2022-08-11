## :sparkler:느낀점/배운점/부족한점



#### BOJ 25304

```python
total_amount = int(input()) # 영수증에 적힌 총 금액
times = int(input()) # 영수증에 적힌 구매한 물건의 종류의 수

for i in range(times):
    a, b = input().split() # a = 각 물건의 가격, b = 개수
    a, b = int(a), int(b)

    total_amount -= (a*b)

print("Yes" if total_amount == 0 else "No") # 영수증의 총 금액과 일치하면 Yes

```





#### BOJ 17388

```python
S, K, H = map(int, input().split())
d = {S: "Soongsil", K: "Korea", H: "Hanyang"}
if sum(d) >= 100: # 세 대학교의 합이 100 이상이면 
    print("OK") # OK 출력
else:
    print(d[min(d)]) # 참여도가 가장 낮은 대학의 동아리 출력
```





#### BOJ 2857

```python
li = []
for i in range(1, 6): # 인덱스 순회
    w = input()
    if "FBI" in w: # FBI 단어가 w에 있으면
        li.append(i) # li에 추가
if li:
    print(*li)
else:
    print("HE GOT AWAY!")
```





#### BOJ 2495

```python
for _ in range(3):
    s = input()
    len_max = 0 # 가장 긴 길이 
    cnt = 1 # 같은 숫자가 나오면 넣음
    for i in range(1, len(s)):
        if s[i-1] == s[i]: # 이전 숫자와 같으면 1씩 증가
            cnt += 1
        else: # 아니면 1
            cnt = 1

        if cnt > len_max: # cnt가 더 큰 숫자이면 max를 cnt로
            len_max = cnt
    print(len_max)


```



#### BOJ 6996

```python
n = int(input())
for _ in range(n):
    a, b = input().split()
    s_a = sorted(a) # sorted 통해서 사전순으로 정렬
    s_b = sorted(b)

    if s_a == s_b: # a와 b 문자열이 같으면 anagrams
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')
```



:sparkles::rocket: for, if, sorted, map 등의 문법을 다양하게 적용시켜서 문제를 풀어볼 수 있어서 좋았습니다. 이론 시간에 배운 DFS 문제는 반복해서 연습을 하는 것이 중요한 것 같고 DFS에 대하여 복합적으로 배울 수 있었습니다.