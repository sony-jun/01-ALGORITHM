soongsil, korea, hanyang = map(int,input().split())
if soongsil + korea + hanyang >= 100 and soongsil != korea != hanyang:
    print('OK')
elif soongsil + korea + hanyang < 100 and soongsil != korea != hanyang:
    if min(soongsil,korea,hanyang) is soongsil:
        print('Soongsil')
    elif min(soongsil,korea,hanyang) is korea:
        print('Korea')
    elif min(soongsil,korea,hanyang) is hanyang:
        print('Hanyang')
