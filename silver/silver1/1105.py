l, r = map(str, input().split())
cnt = 0
if len(l) != len(r):    # 자릿수가 다를 경우 무조건 8의 개수가 0인 수 존재
    print(0)

elif l == r:        # 두 수가 같다면 l의 8의 개수 출력
    print(l.count('8'))

elif l[0] != r[0]:        # 앞자리 수가 다르면 무조건 8의 개수가 0인 수 존재
    print(0)


else:
    if l[0] == '8':
        cnt += 1

    for i in range(1, len(l)):
        if l[i] != r[i]:
            break
        else:
            if l[i] == '8':
                cnt += 1

    print(cnt)