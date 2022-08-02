# input = [3,0,4,0] # len = 4
# input2 = [10,1,3,5,4,0,0,7,0,0,6]

k = int(input())
stack = []
input_list = []
for _ in range(k):
    input_list.append(int(input()))
# for elem in input2:
# print(input_list)
for elem in input_list:
    if elem != 0:
        stack.append(elem)
    else:
        stack.pop()
print(sum(input_list))
