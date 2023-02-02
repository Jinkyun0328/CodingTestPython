def solution(n, k, enemy):
    answer = 0
    
    num = len(enemy)    
    if num <= k:
        return num     

    arrayk = []
    mink = enemy[0]   
    for i in range(k):
        arrayk.append(enemy[i])
        if mink > enemy[i]: 
            mink = enemy[i]

    arrayk = sorted(arrayk)

    for i in range(k, num, 1):
        if mink < enemy[i]:
            n -= mink
            arrayk.append(enemy[i])
            del(arrayk[0])
            arrayk = sorted(arrayk)
            mink = arrayk[0]
        else:
            n -= enemy[i]
            
        if n < 0:
            return i
        
    return num

