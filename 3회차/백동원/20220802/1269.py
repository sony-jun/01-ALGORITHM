A, B = map(int, input().split())
a = set(map(int, input().split()))  # 집합은 영어로 set. 원소의 중복은 허용되지 않음
b = set(map(int, input().split()))  
kyo = a & b                         
hap = a | b                         
result = len(hap) - len(kyo)        # 두 집합의 합집합의 길이에서 교집합의 길이를 뺴면 된다.
print(result)