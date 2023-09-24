# canvas을 전역변수로 선언 
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

# stack class을 선언
class stack: 
    def __init__(self):                 # 생성자
        self.items = []                 # 리스트 생성
        
    def push(self, item):               # push
        self.items.append(item)         # 리스트에 입력값을 추가
        
    def pop(self):                      # pop
        return self.items.pop()         # 가장 마지막에 입력된 값을 반환하고 삭제
    
    def peek(self):                 
        return self.items[-1]           # 가장 위에 있는 변수를 반환
    
    def isEmpty(self):                  # 리스트가 비어 있는지를 확인
        return not self.items           # 비어 있으면 True을 반환

# stack을 사용하여 canvas을 채우는 함수     
def NRFILL(sx, sy, cnt):
    global canvas                       # 전역변수인 canvas을 사용하기 위한 선언
    
    rows = len(canvas)
    cols = len(canvas[0])
    
    stk = stack()                       # 스택 선언. 
    stk.push(cnt)                       # cnt을 push
    stk.push(sy)                        # y좌표 push
    stk.push(sx)                        # x좌표 push
                                        # stack은 입력한 반대순서로 반환되기 때문에
                                        # cnt, y, x 순서대로 push하고 x, y, cnt 순서대로 pop한다.
    
    while not stk.isEmpty():            # stack이 비어있을 때까지 실행
        x = stk.pop()                   # x, y, cnt 순서대로 pop
        y = stk.pop()
        cnt = stk.pop()
        
        if canvas[y][x] != 1:           # canvas가 1이 아니면 반복문의 시작부분으로
            continue
            
        canvas[y][x] = cnt                      # canvas가 1이면 cnt을 저장
        if x + 1 < cols and y + 1 < rows :      # 상하좌우 대각선의 좌표를 stack에 저장   
            stk.push(cnt)
            stk.push(y + 1)
            stk.push(x + 1)

        if x + 1 < cols and y - 1 >= 0 :
            stk.push(cnt)
            stk.push(y - 1)
            stk.push(x + 1)

        if x - 1 >= 0 and y + 1 < rows :
            stk.push(cnt)
            stk.push(y + 1)
            stk.push(x - 1)

        if x - 1 >= 0 and y - 1 >= 0 :
            stk.push(cnt)
            stk.push(y - 1)
            stk.push(x - 1)

        if y + 1 < rows:
            stk.push(cnt)
            stk.push(y + 1)
            stk.push(x)

        if y - 1 >= 0:
            stk.push(cnt)
            stk.push(y - 1)
            stk.push(x)

        if x + 1 < cols:
            stk.push(cnt)
            stk.push(y)
            stk.push(x + 1)

        if x - 1 >= 0:
            stk.push(cnt)
            stk.push(y)
            stk.push(x - 1)

    # canvas의 index로 사용되기 때문에 x, y가 0보다 작아지거나 rows, cols보다 커지지 않도록
    # if문을 사용하여 제한을 걸었다.
    # 현재 좌표를 cnt로 변경한 후 주변 좌표를 stack에 넣으면
    # 다음 반복문을 수행할 때 stack에 저장된 좌표를 pop하여 사용하여
    # 모든 좌표를 확인할 수 있다.

    return


# canvas에서 1의 위치를 반환하는 함수
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


def solution() :
    global canvas

    rows = len(canvas)
    cols = len(canvas[0])

    for i in range(rows):
        print(canvas[i])

    cnt = 1
    while cnt!= 0 :
        x, y, cnt = find(cnt)
        NRFILL(x, y, cnt)

    print()
    print()
    
    for i in range(rows):
        print(canvas[i])

solution()
