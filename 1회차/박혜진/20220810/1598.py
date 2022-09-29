start, end = map(int, input().split())

start = start-1
end = end-1

garo = abs(end // 4 - start // 4)
sero = abs(end % 4 - start % 4)

print(garo + sero)

