from itertools import product

def solution(users, emoticons):
    answer = []

    # 이모티콘의 할인율은 10, 20, 30, 40 중의 하나로 결정된다.
    SaleRate = [10, 20, 30, 40]

    # 이모티콘의 개수만큼 10, 20, 30, 40의 중복이 가능한 조합이 나온다.
    # 이것을 pros에 저장한다. 이모티콘이 4개라면 10, 10, 10, 10 부터 40, 40, 40, 40까지의
    # 중복이 가능한 조합이 pros에 저장된다.
    pros = list(product(SaleRate, repeat=len(emoticons)))

    # 서비스 가입자 index = 0이 가장 크고
    # 그 중에서 매출액 index = 1이 가장 큰 값
    max_sale = [0, 0]

    # 할인율의 조합만큼 반복문을 실행
    # pro에는 10, 10, 10, 10 등이 들어간다.
    for pro in pros:
        # 할인율마다 서비스 가입자와 판매액을 계산.
        sales = [0, 0]

        # users의 길이만큼 반복문을 수행
        # user에는 각 사람별로 이모티콘을 구매하는 할인율과 서비스에 가입하는 금액이 저장되어 있다.
        for user in users:
            # 매출액은 사람별로 구하고 처음 시작을 0으로 설정            
            purchase = 0

            # pro에는 이모티콘의 수만큼 할인율이 저장되어 있다. 
            for i in range (len(pro)):
                # user[0]가 pro[i]보다 작거나 같다면
                # 매출액을 증가시킨다.
                # 100-pro[i]에 emoticons을 100으로 나눈 몫을 곱한다.
                if user[0] <= pro[i]:
                    purchase += ((100-pro[i])*(emoticons[i]//100))

                # 매출액이 user[1]보다 커지면
                # 매출액을 초기화 하고 서비스 가입자를 1 늘린다.
                if purchase >= user[1]:
                    sales[0] += 1
                    break
            else:
                # 매출액이 user[1]보다 커지지 않으면
                # for문이 모두 수행되면 실행된다.
                # sales[1]에 매출액을 더한다.
                sales[1] += purchase

        # 하나의 sales 조합마다 실행한다.
        # 서비스 가입자가 가장 큰 것 중 매출액이 큰 것을 저장한다.
        if sales[0] > max_sale[0]:
            max_sale = sales
        elif sales[0] == max_sale[0] and sales[1] > max_sale[1]:
            max_sale = sales
        
    answer = max_sale
    return answer

#users = [[40, 10000],[25, 10000]]
#emoticons = [7000, 9000]
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons))


