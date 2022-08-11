board = [[0] * 8 for _ in range(8)]
moves = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}

k, s, n = input().split()
ki, kj = 8 - int(k[1]), ord(k[0]) - ord('A')
si, sj = 8 - int(s[1]), ord(s[0]) - ord('A')

for _ in range(int(n)):
    move = input()

    if -1 < ki + moves[move][0] < 8 and -1 < kj + moves[move][1] < 8:
        ki, kj = ki + moves[move][0], kj + moves[move][1]

        if si == ki and sj == kj:
            if -1 < si + moves[move][0] < 8 and -1 < sj + moves[move][1] < 8:
                si, sj = si + moves[move][0], sj + moves[move][1]
            else:
                ki, kj = ki - moves[move][0], kj - moves[move][1]

ki, kj = chr(kj + ord('A')), 8 - ki
si, sj = chr(sj + ord('A')), 8 - si

print(ki + str(kj))
print(si + str(sj))
