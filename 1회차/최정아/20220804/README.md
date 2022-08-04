## :sparkler:느낀점/배운점/부족한점



#### BOJ 1652

```python
def check_row():
    rtn = 0
    for i in range(N):
        c = 0
        for j in range(N+1):
            if arr[i][j] == '.':
                c += 1
            else:
                if c >= 2:
                    rtn += 1
                c = 0
    return rtn

def check_col():
    rtn = 0
    for j in range(N):
        c = 0
        for i in range(N+1):
            if arr[i][j] == '.':
                c += 1
            else:
                if c >= 2:
                    rtn += 1
                c = 0
    return rtn

N = int(input())
arr = [input()+'X' for _ in range(N)]+['X'*(N+1)]
print(check_row(), check_col())
```



#### BOJ 2693

```python
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    # sorted 통해서 정렬
    # 7번째 index 출력
    print(sorted(list(map(int, input().split())))[7])
```



:sparkles::rocket: 반복문과 List Comprehension을 통해서 2차원 리스트를 만드는 연습을 더 많이 해야겠다는 생각을 했고 이차원 리스트를 어제보다는 더 이해한 것 같아서 감사했습니다.