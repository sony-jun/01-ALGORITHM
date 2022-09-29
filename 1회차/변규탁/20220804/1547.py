list_ = [1, 2, 3]

for _ in range(int(input())):
    a, b = map(int, input().split())
    a_ = list_.index(a)
    b_ = list_.index(b)

    list_[a_], list_[b_] = list_[b_], list_[a_]

print(list_[0]) 
    