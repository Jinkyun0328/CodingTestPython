def solution(storey):
    answer = 0
    
    while storey > 0:
        digit = storey % 10
        if digit >= 6:
            storey += (10 - digit)
            answer += (10 - digit)
        elif digit == 5:
            if (storey // 10)%10 >= 5:
                storey += (10 - digit)
                answer += (10 - digit)
            else:
                storey -= digit
                answer += digit
        else:
            storey -= digit
            answer += digit
            
        storey = storey // 10
                
    return answer
