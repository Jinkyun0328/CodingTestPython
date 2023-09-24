from heapq import heappop, heappush

def solution(n, k, enemy):
    answer = 0
    
    num = len(enemy)    
    if num <= k:
        return num     

    arrayk = []
    for i in range(k):
        heappush(arrayk, enemy[i])

    mink = arrayk[0]
    
    for i in range(k, num, 1):
        if mink < enemy[i]:
            n -= mink
            heappush(arrayk, enemy[i])
            heappop(arrayk)
            mink = arrayk[0]
        else:
            n -= enemy[i]
            
        if n < 0:
            return i
        
    return num


from random import randint

n = 500
k = 5
enemy = []
for i in range(20):
    enemy.append(randint(1, 100))

print(enemy)

print(solution(n, k, enemy))
