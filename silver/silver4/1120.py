a, b = map(str, input().split())
result = []
for i in range(len(b)-len(a)+1):        # a와 b의 길이 차이만큼 반복
    cnt = 0
# a = abcd, b = abcdef
# (abcd)ef > cnt = 0
# a(bcde)f > cnt = 4
# ab(cdef) > cnt = 4

    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1

    result.append(cnt)

print(min(result))
