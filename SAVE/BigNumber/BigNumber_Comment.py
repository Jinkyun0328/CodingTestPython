from random import randint

# stack을 사용하기 위한 class
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

def solution(numbers):
    # 스택 생성
    stk = stack()

    # numbers의 길이만큼의 list인 answer을 생성
    answer = [0 for j in range(len(numbers))]

    
    for i in range(0, len(numbers)):
        # 스택이 비어있거나 앞의 수가 뒤의 수보다 큰 경우 index을 push
        if stk.isEmpty() or numbers[i] < numbers[i-1]:
            stk.push(i)
        else:
        # 앞의 수가 뒤의 수보다 작은 경우
            # stack의 가장 마지막에 저장되어 있는 index에 저장된 numbers가
            # i보다 작으면 스택의 값을 pop한 수 answer에 저장
            while (not stk.isEmpty()) and (numbers[stk.peek()] < numbers[i]):
                answer[stk.pop()] = numbers[i]

            # 현재 i값을 스택에 push
            stk.push(i)

    # 스택이 빌 때까지 pop한 후 answer에 -1을 저
    while not stk.isEmpty():
        answer[stk.pop()] = -1
        
    return answer

N = 100
array = []
for i in range(N):
    array.append(randint(1, 1000))

answer = solution(array)
print(answer)
