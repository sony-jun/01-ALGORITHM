
def solution(absolutes, signs):
    numbers = []
    for i in range(len(absolutes)):
        if signs[i] == False:
            numbers.append(absolutes[i]*(-1))
        else:
            numbers.append(absolutes[i])
    answer = sum(numbers)
    return answer

print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))