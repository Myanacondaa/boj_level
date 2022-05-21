s = input()
result = []

for i in range(1, len(s)-1):
    for j in range(i+1, len(s)):
        a = s[:i][::-1]
        b = s[i:j][::-1]
        c = s[j:][::-1]

        result.append(a+b+c)

print(min(result))
