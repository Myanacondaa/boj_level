n, m = map(int, input().split())
dic= {}
for _ in range(n):
    k, v = map(str, input().split())
    dic[k] = v

for _ in range(m):
    link = input()
    print(dic[link])