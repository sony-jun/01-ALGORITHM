## :sparkler:느낀점/배운점/부족한점



#### BOJ 2609 최대공약수와 최소공배수

```python
# 최대공약수와 최소공배수 구함
# 유클리드 호제법 사용

# 최대공약수
def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a
# 최소공배수    
def lcm(a,b) :
    return int(a*b/gcd(a,b))

# 입력받은 자연수를 문자열 타입에서 정수형 타입으로 바꿈
a,b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))
```



#### BOJ 2331 분해합

```python
# 초기값 N 설정
N = int(input())
# 생성자 초기값 설정
ans = 0
# 최소 수부터 생성자 찾음
start = max(N - 9 * len(str(N)), 0)
# 0부터 N까지 생성자 찾음
for i in range(start, N):
    if N == sum(map(int, str(i))) + i:
        ans = i # 첫번째 생성자 나타나면 중지
        break
print(ans)
```



#### BOJ 2846 오르막길

```python
N = int(input())
numlist = list(map(int, input().split()))

# pre는 원래 높이를 뜻함
pre = numlist[0]
high = 0
res = 0
for i in numlist:
    if pre < i: # pre보다 크면
        high += i - pre #오름
    
    else: # 아니면
        res = max(res, high) #내림
        high = 0
    pre = i

print(max(high, res))

```



#### BOJ 2953 나는 요리사다

```python
# 예제 입력은 contestant에 넣음
contestant = []
cont_sum = []
for a in range(5):
    # map함수 사용해서 contestant에 담음
    contestant.append(list(map(int, input().split())))
    # index에 따른 각 숫자들의 합을 구함
    cont_sum.append(sum(contestant[a]))
# 가장 큰 수의 index와 숫자 출력
print(cont_sum.index(max(cont_sum))+1, max(cont_sum))
```



:sparkles::rocket: 문제마다 input(), map 함수, for문, def 정의, append method 등 수업에서 배운 내용을 적용하여 다양한 문제에 접근하는 것을 배웠습니다. 이전에는 접근 방법의 정확도가 얼마 되지 않았다면 문제 풀이를 하면서 정확도가 성장하는 것을 느낄 수 있었습니다.