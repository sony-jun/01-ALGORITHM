# 애너그램 🐳
# 문제 : A에 속하는 알파벳의 순서를 바꿔 B를 만들 수 있다면 애너그램, 애너그램인지 아닌지를 구하기

N = int(input())

for _ in range(N):
    A, B = input().split()

    a = sorted(list(A))
    b = sorted(list(B))

    if a == b:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')
