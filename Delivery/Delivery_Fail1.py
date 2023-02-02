# 배열에서 0이 아닌 수가 저장된 가장 큰 index을 반환하는 함수
def func_a(arr, n):
    for i in range(n-1, -1, -1):
        if arr[i] > 0:
            return i

    return -1


def solution(cap, n, deliveries, pickups):
    answer = 0

    # 배열에서 0이 아닌 수가 저장된 가장 큰 인덱스
    del_max = func_a(deliveries, n)
    pick_max = func_a(pickups, n)
    
    # deliveries와 pickups 중 하나라도 0이 아닌 수가 있으면
    # 반복문을 수행
    while del_max >= 0 or pick_max >= 0:
        # del_max와 pick_max 중 더 큰 수 x2만큼 answer에 더해진다.
        # answer.append(max(del_max, pick_max))

        answer += (max(del_max, pick_max)+1)*2
        
        if del_max >= 0:
            if deliveries[del_max] > cap:
                deliveries[del_max] -= cap

            else :
                sub = cap
                for i in range(del_max, -1, -1):
                    if deliveries[i] < sub:
                        sub -= deliveries[i]
                        deliveries[i] = 0
                    else:
                        deliveries[i] -= sub
                        break
                           
        if pick_max >= 0:
            if pickups[pick_max] > cap:
                pickups[pick_max] -= cap

            else :
                sub = cap
                for i in range(pick_max, -1, -1):
                    if pickups[i] < sub:
                        sub -= pickups[i]
                        pickups[i] = 0
                    else:
                        pickups[i] -= sub
                        break
                                       
        del_max = func_a(deliveries, n)
        pick_max = func_a(pickups, n)
        

    return answer
