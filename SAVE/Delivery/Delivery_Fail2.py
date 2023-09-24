def solution(cap, n, deliveries, pickups):
    answer = 0

    # 가장 멀리 있는 곳부터 간다.
    # 가는 길에 배달을 하고 오는 길에 수거를 한다.
    # 가장 멀리 있는 index부터 cap만큼 감소시킨다.

    # 역순으로 변환
    redel = deliveries[::-1]
    repick = pickups[::-1]

    # 누적으로 변환
    for i in range(1, n):
        redel[i] += redel[i - 1]
        repick[i] += repick[i - 1]

    
    for i in range(0, n):
        redel[i] = (redel[i]+cap-1)//cap
        repick[i] = (repick[i]+cap-1)//cap

    arrayA = []
    arrayB = []

    if redel[0] > 0:
        for i in range(redel[0]):
            arrayA.append(0)

    for i in range(1, n):
        sub = redel[i] > redel[i - 1]
        if sub > 0:
            for j in range(sub):
                arrayA.append(i)

    if repick[0] > 0:
        for i in range(repick[0]):
            arrayB.append(0)

    for i in range(1, n):
        sub = repick[i] > repick[i - 1]
        if sub > 0:
            for j in range(sub):
                arrayB.append(i)
    
    for i in range(len(arrayA)):
        arrayA[i] = n - arrayA[i]

    for i in range(len(arrayB)):
        arrayB[i] = n - arrayB[i]


    min1 = min(len(arrayA), len(arrayB))
    max1 = max(len(arrayA), len(arrayB))

    for i in range(min1):
        answer = answer + (2*max(arrayA[i], arrayB[i]))

    if len(arrayA) > len(arrayB):
        for i in range(min1, max1):
            answer = answer + (2*arrayA[i])

    else:
        for i in range(min1, max1):
            answer = answer + (2*arrayB[i])
   
    return answer


deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
n = 5
cap = 4

answer = solution(cap, n, deliveries, pickups)
print(answer)
