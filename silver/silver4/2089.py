n = int(input())
res = ''

if n == 0:
    print(0)

else:
    while n:        # n이 0이 아닐때까지
        if n % (-2):    # -2로 나눈 뒤  , 나머지가 1일 경우
            res = '1'+res   # 앞에 붙임
            n = (n//-2)+1
        else:
            res = '0'+res
            n //= -2

    print(res)
