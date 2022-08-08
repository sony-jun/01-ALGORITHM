computer = [0]
for i in range(100):
    computer += [0]
cnt = int(input())
guest = list(map(int, input().split()))
refuse = 0
for i in guest:
    if computer[i] == 0:
        computer[i] = 1
    else:
        refuse += 1
print(refuse)