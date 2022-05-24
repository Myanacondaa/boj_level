document = input()
n = input()
cnt = 0
tmp = 0
while tmp <= len(document)-len(n):
    res = document[tmp:tmp+len(n)]
    if n == res:
        cnt += 1
        tmp += len(n)
    else:
        tmp += 1

print(cnt)