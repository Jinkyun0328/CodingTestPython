def solution(r1, r2):
    answer = 0
    
    for i in range(-r2, r2+1, 1):
        for j in range(-r2, r2+1, 1):
            if (i*i + j*j) >= r1*r1 and (i*i + j*j) <= r2*r2:
                answer += 1

    return answer
