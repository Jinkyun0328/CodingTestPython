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


class stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return not self.items

    
def NRFILL(sx, sy, cnt):
    global canvas
    
    rows = len(canvas)
    cols = len(canvas[0])
    
    stk = stack()
    stk.push(cnt)
    stk.push(sy)
    stk.push(sx)
    
    while not stk.isEmpty():
        x = stk.pop()
        y = stk.pop()
        cnt = stk.pop()
        
        if canvas[y][x] != 1:
            continue
            
        canvas[y][x] = cnt
        if x + 1 < cols and y + 1 < rows :
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

    return


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
