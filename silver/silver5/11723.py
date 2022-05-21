n = int(input())
s = set()
for i in range(n):
    x = list(map(str, input().split()))

    if len(x) == 1:
        if x[0] == "all":
            s = {i for i in range(1, 21)}

        else:
            s.clear()

    else:
        x[1] = int(x[1])
        if x[0] == "add":
            s.add(x[1])
        elif x[0] == "remove":
            s.remove(x[1])
        elif x[0] == "check":
            print(1 if x[1] in s else 0)

        elif x[0] == "toggle":
            if x[1] in s:
                s.remove(x[1])
            else:
                s.add(x[1])

