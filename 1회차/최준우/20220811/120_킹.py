# https://www.acmicpc.net/problem/1063

K, S, N = input().split()
K = list(K)
K[1] = int(K[1])
S = list(S)
S[1] = int(S[1])

for _ in range(int(N)):
    print(K[0], K[1], sep = '')
    print(S[0], S[1], sep = '')
    direction = input()
    
    if direction == 'R': # R
        temp_x = chr(ord(K[0])+1)
        if ord(temp_x) > ord('H'):
            continue
        if temp_x == S[0] and K[1] == S[1]:
            temp_sx = chr(ord(S[0])+1)
            if ord(temp_x) > ord('H'):
                continue
            else:
                S[0] = temp_sx
        K[0] = temp_x

    elif direction == 'L': # L
        temp_x = chr(ord(K[0])-1)
        if ord(temp_x) < ord('A'):
            continue
        if temp_x == S[0] and K[1] == S[1]:
            temp_sx = chr(ord(S[0])-1)
            if ord(temp_x) < ord('A'):
                continue
            else:
                S[0] = temp_sx
        K[0] = temp_x
        
    elif direction == 'B': # B
        temp_y = K[1]-1
        if temp_y < 1:
            continue
        if temp_y == S[1] and K[0] == S[0]:
            temp_sy = S[1]-1
            if temp_sy < 1:
                continue
            else:
                S[1] = temp_sy
        K[1] = temp_y

    elif direction == 'T': # T
        temp_y = K[1]+1
        if temp_y > 8:
            continue
        if temp_y == S[1] and K[0] == S[0]:
            temp_sy = S[1]+1
            if temp_sy > 8:
                continue
            else:
                S[1] = temp_sy
        K[1] = temp_y

    elif direction == 'RT': # RT
        temp_x = chr(ord(K[0])+1)
        temp_y = K[1]+1
        if ord(temp_x) > ord('H') or temp_y > 8:
            continue
        if (temp_x == S[0] and K[1] == S[1]) or (temp_y == S[1] and K[0] == S[0]):
            temp_sx = chr(ord(S[0])+1)
            temp_sy = S[1]+1
            if ord(temp_x) > ord('H') or temp_sy > 8:
                continue
            else:
                S[0] = temp_sx
                S[1] = temp_sy
        K[0] = temp_x
        K[1] = temp_y

    elif direction == 'LT': # LT
        temp_x = chr(ord(K[0])-1)
        temp_y = K[1]+1
        if ord(temp_x) < ord('A') or temp_y > 8:
            continue
        if (temp_x == S[0] and K[1] == S[1]) or (temp_y == S[1] and K[0] == S[0]):
            temp_sx = chr(ord(S[0])-1)
            temp_sy = S[1]+1
            if ord(temp_x) < ord('A') or temp_sy > 8:
                continue
            else:
                S[0] = temp_sx
                S[1] = temp_sy
        K[0] = temp_x
        K[1] = temp_y

    elif direction == 'RB': # RB
        temp_x = chr(ord(K[0])+1)
        temp_y = K[1]-1
        if ord(temp_x) > ord('H') or temp_y < 1:
            continue
        if (temp_x == S[0] and temp_y == S[1]):
            temp_sx = chr(ord(S[0])+1)
            temp_sy = S[1]-1
            if ord(temp_x) > ord('H') or temp_sy < 1:
                continue
            else:
                S[0] = temp_sx
                S[1] = temp_sy
        K[0] = temp_x
        K[1] = temp_y

    elif direction == 'LB': # LB
        temp_x = chr(ord(K[0])-1)
        temp_y = K[1]-1
        if ord(temp_x) < ord('A') or temp_y < 1:
            continue
        if (temp_x == S[0] and K[1] == S[1]) or (temp_y == S[1] and K[0] == S[0]):
            temp_sx = chr(ord(S[0])-1)
            temp_sy = S[1]-1
            if ord(temp_x) < ord('A') or temp_sy < 1:
                continue
            else:
                S[0] = temp_sx
                S[1] = temp_sy
        K[0] = temp_x
        K[1] = temp_y
print(K[0], K[1], sep = '')
print(S[0], S[1], sep = '')