# a = ['1', '2', '4']
# b = ['2', '3', '4', '5', '6']
a, b = map(int, input().split())
set_1 = set((map(int, input().split())))
set_2 = set((map(int, input().split())))
print(len(set_1 ^ set_2))

# a_b = set_1 - set_2
# b_a = set_2 - set_1
# print(len(a_b) + len(b_a))