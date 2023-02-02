def solution(cap, n, deliveries, pickups):
    def get_points(array):
        points = []
        box, index = 0, n - 1

        while index > -1:
            if array[index] == 0:
                index -= 1
                continue
            if box == 0:
                points.append(index)
            capacity = cap - box
            if array[index] <= capacity:
                box += array[index]
                index -= 1
            else:
                array[index] -= capacity
                box = 0
        return iter(points), len(points)

    answer = 0
    (d_points, d_length), (p_points, p_length) = get_points(deliveries), get_points(pickups)

    for _ in range(max(d_length, p_length)):
        answer += max(next(d_points, 0), next(p_points, 0))+1

    return answer * 2

    
