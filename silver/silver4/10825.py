n = int(input())
classroom = []
for _ in range(n):
    classroom.append(list(map(str, input().split())))

classroom.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(classroom[i][0])