n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
price = 0

for i in range(n):
    if i % 3 != 2:
        price += arr[i]

print(price)