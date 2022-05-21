num, snake = map(int, input().split())
fruit = list(map(int, input().split()))
fruit.sort()

for i in range(len(fruit)):
    if snake >= fruit[i]:
        snake += 1
    else:
        break

print(snake)