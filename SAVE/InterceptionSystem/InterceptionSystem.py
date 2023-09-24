def solution(targets):
    answer = 0
    bound = 0

    for s, e in sorted(targets):
        if bound > s:
            bound = min(bound, e)
        else:
            bound = e
            answer += 1

    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))


# targets에 들어있는 구간에서 최소요격횟수를 구해야 한다.
# 최대한 겹치도록 요격하는 구간을 정한다.

# bound은 경계를 의미한다.
# bound가 s보다 크다는 것은 요격하는 지점이 시작지점보다 크다는 것이고
# 이때 bound와 e중 더 작은 값을 bound로 설정한다.

# bound가 s보다 작다면 즉 현재 bound에서 더 이상 요격할 수 있는 지점이 없다면
# bound을 현재 값의 e로 설정하고 answer에 1을 더한다.
