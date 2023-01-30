# 코딩테스트 '무인도여행'
# 격자의 각 칸에는 X 또는 1~9의 자연수가 적혀있다.
# 지도에서 X는 바다이며 숫자는 무인도를 나타낸다.
# 지도의 각 칸에 적인 숫자는 식량을 나타낸다.
# 상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도를 이룬다.
# 최대 며칠씩 머무를 수 있는지 오름차순에 담아 return하는 solution 함수를 완성하시오.

############################################################
# 연결된 1을 같은 색으로 칠하는 코드인 NRFILL을 응요했다.
# 1. map은 최대 100x100이므로 100x100의 canvas을 전역변수로 설정
# 2. stack을 사용하기 위한 class을 선언
# 3. maps에 저장된 문자가 X이면 canvas에 0을 저장하고 1~9 사이의 문자면 1을 저장
# 4. 1~9의 문자는 아스키코드 ord()가 49에서 57 사이
# 5. NRFILL 함수를 사용하여 canvas에서 상하좌우로 연결된 1에 같은 숫자를 저장
# 6. canvas의 max값을 구한 후
# 7. canvas에 같은 값이 저장되어 있는 좌표의 ord(maps) - 48을 더해서 answer에 저장
# 8. 7의 과정을 2부터 max까지 수행
# 9. answer을 오름차순으로 정렬


# maps은 최대 100x100의 matrix이다.
canvas = [[0 for x in range(100)] for y in range(100)]


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
def NRFILL(sx, sy, rows, cols, cnt):
    global canvas
    
    stk = stack()                       
    stk.push(cnt)                       
    stk.push(sy)                        
    stk.push(sx)                       

    while not stk.isEmpty():            # stack이 비어있을 때까지 실행
        x = stk.pop()                   # x, y, cnt 순서대로 pop
        y = stk.pop()
        cnt = stk.pop()
        
        if canvas[y][x] != 1:          
            continue
            
        canvas[y][x] = cnt                     

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

# canvas에서 1의 위치를 반환하는 함수
def find(rows, cols, cnt):
    global canvas
    
    for sy in range(rows):
        for sx in range(cols):
            if canvas[sy][sx] == 1:
                cnt += 1
                return sx, sy, cnt
    cnt = 0
    return 0, 0, cnt

def maps_to_canvas(maps, rows, cols):
    global canvas
    
    for y in range(rows):
        for x in range(cols):
            if ord(maps[y][x]) >= 49 and ord(maps[y][x]) <= 57:
                canvas[y][x] = 1
            elif maps[y][x] == 'X':
                canvas[y][x] = 0
            else:
                canvas[y][x] = -1
                
    return

def solution(maps):
    global canvas
    answer = []
    
    # maps의 길이 구하기
    rows = len(maps)
    cols = len(maps[0])
    
    # maps가 X이면 canvas에 0을 저장
    # maps가 1~9이면 canvas에 1을 저장
    maps_to_canvas(maps, rows, cols)
    
    # 상하좌우로 이어진 1이 있을 경우 같은 숫자로 채움
    cnt = 1
    while cnt != 0:
        sx, sy, cnt = find(rows, cols, cnt)
        NRFILL(sx, sy, rows, cols, cnt)
    
    # canvas의 최댓값을 구함
    max = 0
    for y in range(rows):
        for x in range(cols):
            if canvas[y][x] > max:
                max = canvas[y][x]
                
    if max == 0:
        answer.append(-1)
        return answer
    
    for i in range(2, max+1):
        sum = 0
        for y in range(rows):
            for x in range(cols):
                if canvas[y][x] == i:
                    sum += (ord(maps[y][x]) - 48)
                    
        answer.append(sum)
    
    for i in range(0, len(answer)-1, 1):
        for j in range(i+1, len(answer), 1):
            if answer[i] > answer[j]:
                tmp = answer[j]
                answer[j] = answer[i]
                answer[i] = tmp
    
    return answer
