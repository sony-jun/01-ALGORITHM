## :sparkler:느낀점/배운점/부족한점



#### BOJ 9325

```python
for _ in range(int(input())):
    s = int(input()) # 자동차의 가격 s
    for _ in range(int(input())): # for 반복문 통해 s 순회
        q, p = map(int, input().split()) # 특정 옵션의 개수 q와 해당 옵션의 가격 p int로 형변환
        s += q*p # s에 qxp의 값을 증가시킴
    print(s)
```



#### BOJ 3046

```python
R1, S = map(int, input().split()) # 정수 R1과 S를 split하고 정수형으로 변환
R2 = S*2 - R1
print(R2)
```



#### BOJ 1453

```python
n = int(input()) # 손님의 수 N이 주어짐
seat = map(int, input().split()) # 원하는 자리 정수형으로 변환
pc = [0]*101
reject_cus = 0 # 거절당하는 손님

for a in seat:
    if(pc[a] == 0): # 원하는 자리 비어있으면
        pc[a] += 1
    else:
        reject_cus += 1
        
print(reject_cus)
```



:sparkles::rocket: map 함수와 for, if문을 사용할 수 있어서 복습에 도움이 많이 되었고 기초 실력이 향상하는 것 같았습니다.  완전 탐색과 델타 탐색을 응용하는 문제도 다시 한 번 과정을 단계별로 그려보면서 문제에 적용하고 연습해 나가야 겠습니다.