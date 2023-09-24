def solution(n, l, r):
    answer = 0
    
    bits = ''
    before = '1'
    for i in range(n):
        bits = ''
        for j in before:
            if j == '0':
                bits += "00000"
            elif j == '1':
                bits += "11011"
                
        before = bits
    
    for i in range(l-1, r, 1):
        if bits[i] == '1':
            answer += 1
    
    return answer
