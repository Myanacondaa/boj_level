
n = int(input())
dic = {}
for _ in range(n):
    num = int(input())
    if num in dic.keys():
        dic[num] += 1
    else:
        dic[num] = 1

result = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
