t = int(input())

for _ in range(t):
	l = input().split()
	for i in l:
		print(i[::-1], end = ' ')
	print()
