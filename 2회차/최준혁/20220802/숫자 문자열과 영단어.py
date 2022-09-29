# 0	zero
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine


def solution(s):
    int_dic = {"zero":0, "one":1, "two":2, "three":3, "four":4,
            "five":5, "six":6, "seven":7, "eight":8, "nine":9
        }
    answer = s
    for k, v in int_dic.items():
        answer = answer.replace(k, str(v))
    return int(answer)

S = input()
print(solution(S))