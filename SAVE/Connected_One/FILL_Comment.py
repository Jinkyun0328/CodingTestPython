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

# canvas에 있는 1을 찾는 함수
def find(cnt):
    # 전역변수인 canvas을 사용하기 위해 canvas을 global을 사용하여 선언
    global canvas

    rows = len(canvas)      # canvas의 행 (세로길이)
    cols = len(canvas[0])   # canvas의 열 (가로길이)

    for sy in range(rows):
        for sx in range(cols):
            if canvas[sy][sx] == 1:     # canvas에 1이 있으면
                cnt += 1                # cnt에 1을 더한 후
                return sx, sy, cnt      # 좌표와 cnt을 반환
    cnt = 0                             # canvas에 1이 없으면
    return 0, 0, cnt                    # cnt을 0으로 한 후 0을 반

# 재귀함수를 사용하여 canvas을 채우는 함수
def FILL(x, y, cnt):
    global canvas

    rows = len(canvas)
    cols = len(canvas[0])

    if canvas[y][x] == 1:                   # canvas가 1이면
        canvas[y][x] = cnt                  # canvas의 값을 cnt로 변경

        # if를 사용하지 않으면 index의 허용범위가 벗어난다는 오류가 발생
        # 상하좌우 대각선 방향으로 FILL 함수를 실행
        # 근처에 1이 있으면 같은 cnt로 변경하기 위한 재귀함수
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

    else:                                   # 1이 아니면 return
        return

# 함수를 실행하고 canvas을 출력하는 함수
def solution() :
    global canvas

    rows = len(canvas)
    cols = len(canvas[0])

    for i in range(rows):           # canvas의 원본 출력
        print(canvas[i])

    cnt = 1
    while cnt != 0:                 # cnt가 0이 아닐 때까지 즉 1이 없을 때까지 실행
        x, y, cnt = find(cnt)       # 1의 위치를 찾아 x, y에 저장
        FILL(x, y, cnt)             # FILL 함수 실행


    print()
    print()
    
    for i in range(rows):           # 바뀐 canvas 출력
        print(canvas[i])

solution()
