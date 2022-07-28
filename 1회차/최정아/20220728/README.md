## :sparkler:느낀점/배운점/부족한점



#### BOJ 23825 SASA 모형을 만들어보자

```python
n, m = map(int, input().split())
# 가장 작은 값을 선정
sasa = min(n, m)
# 2로 나눈 뒤 몫 출력
print(sasa//2)
```



#### BOJ 3052 나머지

```python
# set은 집합 선언하고, {} 형태로 저장된다
# set은 중복되는 값들은 1개로 처리
a=set()

# add() 사용해서 집합 요소 추가
for i in range(10):
    # input을 통해 받은 값을 정수형으로 바꾸고 
    # 42로 나눈 나머지 값을 추가
    # 이 때 중복되는 값들은 1개로 처리
    a.add(int(input())%42)

print(len(a))
```



#### BOJ 1297 쉽게 푸는 문제

```python
a, b = map(int, input().split())
# section은 1,000 이상인 a,b의 범위
section = [[i]*i for i in range(1, 46)]
section = [0] + sum(section, [])
# a와 b의 구간의 합
print(sum(section[a:b+1]))
```



:sparkles::rocket: map, set 함수를 문제에 응용하는 것을 배웠습니다. 함수 자체를 개념으로 배운 후에 문제에 적용을 해서 배우니 map과 set 함수의 용도가 더욱 선명하게 그려지는 느낌입니다. 이론 시간에 배운 내용을 더 사용해야 겠다는 생각을 했습니다.