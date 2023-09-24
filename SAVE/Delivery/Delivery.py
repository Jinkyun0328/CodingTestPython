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
        return points[::-1]

    answer = 0
    d_points, p_points = get_points(deliveries), get_points(pickups)
    while d_points or p_points:
        answer += max(d_points.pop() if d_points else 0, p_points.pop() if p_points else 0) + 1

    return answer * 2

    
