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
    stk = stack()
    answer = [0 for j in range(len(numbers))]
    
    for i in range(0, len(numbers)):
        if stk.isEmpty() or numbers[i] < numbers[i-1]:
            stk.push(i)
        else:
            while (not stk.isEmpty()) and (numbers[stk.peek()] < numbers[i]):
                answer[stk.pop()] = numbers[i]
                
            stk.push(i)
    while not stk.isEmpty():
        answer[stk.pop()] = -1
        
    return answer
