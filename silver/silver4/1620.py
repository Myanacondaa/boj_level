import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for i in range(1, n+1):
    pocketmon = input().rstrip()
    dic[i] = pocketmon
    dic[pocketmon] = i
for i in range(m):
    x = input().rstrip()
    if x.isdigit():
        print(dic[int(x)])
    else:
        print(dic[x])

