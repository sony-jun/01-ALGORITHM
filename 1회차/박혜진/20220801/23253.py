# IndexError 코드
# n권과 m개의 더미를 입력받기
n, m = map(int, input().split())

# 각 더미를 입력받을 리스트 만들기
stack_ = []

# 입력받은 더미 m개에 각각 정보를 저장
for i in range(m) :
  # 각 더미에 입력받을 책 권수
  book = int(input())
  # 각 더미에 저장될 책 번호를 입력받은 순서대로 리스트에 저장
  stack_.append(list(map(int, input().split())))

# print(stack_)

# m개의 더미에서 번갈아가며 숫자를 꺼내어 비교
# 1부터 n까지의 수를 순서대로 꺼내려면 더미 1의 숫자가 더미 2의 숫자보다 작아야한다.
# 같은 줄의 더미 1의 숫자가 더미 2의 숫자보다 작으면 Yes 아니라면 No
while True :
  for i in range(m) :
    for o in range(len(stack_[i])) :
      if stack_[i][o] < stack_[i+1][o] :
        print('Yes')
        break
      else :
        print('No')
        break

# 정답 코드
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

list_2 = []
for i in range(m):
    a = int(input())
    list_number = list(map(int,input().split()))
    for j in range(0,len(list_number)-1):
        if list_number[j] < list_number[j+1]:
            list_2.append(list_number[j+1])
        
            
if list_2 == []:
    print('Yes')
else:
    print('No')