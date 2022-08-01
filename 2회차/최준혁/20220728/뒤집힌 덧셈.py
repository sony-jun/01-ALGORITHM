A, B = map(list, input().split())

def Rev(x):
    rev = ''
    for i in range(len(x)-1, -1, -1): # 인덱스의 역순으로 진행
        rev += x[i] # 뒤집은 값을 rev에 누적해서 저장
    return int(rev) # int로 리턴해줌

rev_c = Rev(A) + Rev(B) # 더해서 저장
result = Rev(str(rev_c)) # 함수 사용을 위해 str로 변환 후 실행
print(result)