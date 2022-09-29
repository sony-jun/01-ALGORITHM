## :sparkler:느낀점/배운점/부족한점



#### 2577 숫자의 개수

```python
a = int(input()) #150 
b = int(input()) #266
c = int(input()) #427
# 곱한 정수 값은 str으로 바꾼뒤에 리스트로 만든다
result = list(str(a * b * c)) #[1, 7, 0, 3, 7, 3, 0, 0]

for i in range(10): # i는 0~9까지 순회
    #정수 타입을 문자열 타입으로 바꾸는 이유는 cnt 함수 사용하기 위함
    print(result.count(str(i))) #i는 문자열 타입으로 바꿔서 count.
```



#### 2908 상수

```python
# input은 기본적으로 문자열 받음
a, b = input().split()
# 리스트 슬라이싱해서 숫자 거꾸로 나열
a = int(a[::-1])
b = int(b[::-1])

# 만약 a가 b보다 크면 a 출력
# 아니면 b출력
if a > b:
    print(a)
else:
    print(b)
```



#### 8958 OX 퀴즈

```python
# input 문자열을 정수 타입으로 변환
n = int(input())
# index로 접근해서 각 숫자 순회
for i in range(n):
    x = str(input())
    sum = 0
    cnt = 0
    # for문 안에 for문 생성
    for j in list(x):
        # 0을 만나면 
        if j == 'O':
            # 1 더함
            cnt += 1
            # 그 값을 sum에 담음
            sum += cnt
        else:
            cnt = 0
    print(sum)
```



:sparkles::rocket: 조건문, 반복문, 알고리즘 활용하는 것을 문제를 통해서 배웠습니다. input(), count, 리스트 슬라이싱 등의 함수를 사용했는데 함수에 따른 타입 변환을 더 연습해야겠다고 생각했습니다.