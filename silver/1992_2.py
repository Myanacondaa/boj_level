
n = int(input())
video = []
for _ in range(n):
    col = list(map(int, input()))
    video.append(col)


def zip_video_with_quad_tree(x, y, n):
    check = video[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != video[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n //= 2
        zip_video_with_quad_tree(x, y, n)
        zip_video_with_quad_tree(x, y+n, n)
        zip_video_with_quad_tree(x+n, y, n)
        zip_video_with_quad_tree(x+n, y+n, n)
        print(")", end='')

    elif check == 1:
        print(1, end='')

    else:
        print(0, end='')


zip_video_with_quad_tree(0, 0, n)


