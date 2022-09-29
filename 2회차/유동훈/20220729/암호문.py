for i in range(1, 11):
    
    N = input()
    ori_crypt = input().split()
    n = int(input())
    command = input().split()
    mod_crypt = []

    cnt = 2
    for j in range(n):
        ori_str = ''.join(ori_crypt[int(command[cnt-1])]) # cnt번째 명령어에서 말하고 있는 원본 암호문의 x번째 위치한 숫자
        ori_crypt = ' '.join(ori_crypt)
        mod_str = ' '.join(command[cnt+1:cnt+1+int(command[cnt])]) # 
        mod_str = ori_str + ' ' + mod_str
        ori_crypt = ori_crypt.replace(ori_str, mod_str)

        cnt += int(command[cnt]) + 3
        

        # ['449047', '855428', '400905', '139831', '966064', '336948', '119288', '425117', '532416', '358612', '929816', '313459', '311433', '472478', '589139', '568205']
    
    # print(list(mod_crypt.split())[0])

    print(f'#{i}', end=' ')
    for k in range(10):
        print(list(mod_crypt.split())[k], end=' ')
    # answer = []
    # for j in range(10):
    #     answer = answer.append(list(mod_crypt.split())[j])
    #     print(answer)
    # #     answer = ''.join(answer)
    # # print(f'#{i} {answer}', end=' ')
