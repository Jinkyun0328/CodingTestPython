# canvas 전역변수로 선언
canvas = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
          [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
          [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
          [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
          [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
          [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
          [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
          [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
          [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def find(cnt):
    global canvas

    rows = len(canvas)
    cols = len(canvas[0])

    for sy in range(rows):
        for sx in range(cols):
            if canvas[sy][sx] == 1:
                cnt += 1
                return sx, sy, cnt
    cnt = 0
    return 0, 0, cnt

def FILL(x, y, cnt):
    global canvas

    rows = len(canvas)
    cols = len(canvas[0])

    if canvas[y][x] == 1:
        canvas[y][x] = cnt

        if x - 1 >= 0:
            FILL(x - 1, y, cnt)

        if x + 1 < cols:
            FILL(x + 1, y, cnt)

        if y - 1 >= 0:
            FILL(x, y - 1, cnt)

        if y + 1 < rows:
            FILL(x, y + 1, cnt)

        if x - 1 >= 0 and y - 1 >= 0:
            FILL(x - 1, y - 1, cnt)

        if x - 1 >= 0 and y + 1 < rows:
            FILL(x - 1, y + 1, cnt)

        if x + 1 < cols and y - 1 >= 0:
            FILL(x + 1, y - 1, cnt)

        if x + 1 < cols and y + 1 < rows:
            FILL(x + 1, y + 1, cnt)

    else:
        return

def solution() :
    global canvas

    rows = len(canvas)
    cols = len(canvas[0])

    for i in range(rows):
        print(canvas[i])

    cnt = 1
    while cnt != 0:
        x, y, cnt = find(cnt)
        FILL(x, y, cnt)


    print()
    print()
    
    for i in range(rows):
        print(canvas[i])

solution()
