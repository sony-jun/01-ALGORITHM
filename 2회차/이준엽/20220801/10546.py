import sys
input = sys.stdin.readline

n = int(input())

result = {}
for i in range(n):
    start_peron = input()
    if start_peron in result:
        result[start_peron] +=1
    else:
        result[start_peron] = 1
for i in range(n-1):
    end_person = input()
    result[end_person] -=1
for i in result:
    if result[i]:
        print(i)
        break
# answer = [k for k,v in result.items() if v == 1]
# print(answer[0])

# for i in result:
#     if result[i]:
#         print(result[i])



# import sys
# input = sys.stdin.readline

# n = int(input())
# start_people = [input() for i in range(n)]

# end_people = [input() for i in range(n-1)]

# for i in end_people:
#     start_people.remove(i)
# print(start_people[0])