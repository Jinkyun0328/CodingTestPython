def solution(data, col, row_begin, row_end):
    answer = 0
    
    rows = len(data)
    for i in range(0, rows - 1, 1):
        for j in range(i + 1, rows, 1):
            if data[i][col-1] > data[j][col-1]:
                data[i], data[j] = data[j], data[i]
            elif data[i][col-1] == data[j][col-1]:
                if data[i][0] < data[j][0]:
                    data[i], data[j] = data[j], data[i]

    # print(data)
    xor = 0
    for i in range(row_begin - 1, row_end, 1):
        S = 0
        for j in data[i]:
            S += j % (i + 1)
        
        xor = xor ^ S
    
    answer = xor
    return answer

data = [[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]]
col = 2
row_begin = 2
row_end = 3
print(solution(data, col, row_begin, row_end))
