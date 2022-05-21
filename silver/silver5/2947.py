#   버블 정렬

tree = list(map(int, input().split()))

for i in range(len(tree)-1):
    for j in range(len(tree)-1):
        if tree[j] > tree[j+1]:
            tree[j], tree[j+1] = tree[j+1], tree[j]
            for t in tree:
                print(t, end= ' ')
            print()