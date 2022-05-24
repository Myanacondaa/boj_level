s = input()
result = []
for _ in s:
    result.append(s)
    s = s[1:]

for ele in sorted(result):
    print(ele)