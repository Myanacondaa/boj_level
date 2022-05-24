n, m = map(int, input().split())        # 듣도, 보도
listen = set()
see = set()
for _ in range(n):
    listen.add(input())
for _ in range(m):
    see.add(input())
result = listen & see       # 듣도 보도 못한 사람은 두 집합의 교집합

print(len(result))
for ele in sorted(result):
    print(ele, end=' ')