from itertools import combinations
while True:
    arr = list(map(int, input().split()))
    if arr != [0]:
        arr.pop(0)
        combi = list(combinations(arr, 6))
        for ele in combi:
            for e in ele:
                print(e, end=' ')
            print()

        print()

    else:
        exit(0)