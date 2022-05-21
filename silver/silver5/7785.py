n = int(input())
dic= {}         # 리스트 쓰면 시간 초과, remove() 함수가 O(n)
for i in range(n):
    name, in_out = map(str, input().split())
    if in_out == "enter":
        dic[name] = 1
    else:
        del dic[name]

s = sorted(dic.keys(), reverse=True)
for n in s:
    print(n)