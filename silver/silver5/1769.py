count = 0


def recursive(x: str):
    global count
    if len(x) == 1:
        if int(x) % 3 == 0:
            print(count)
            print("YES")
            exit(0)
        else:
            print(count)
            print('NO')
            exit(0)

    sum_x = 0
    for i in range(len(x)):
        sum_x += int(x[i])

    count += 1
    recursive(str(sum_x))


n = input()
recursive(n)