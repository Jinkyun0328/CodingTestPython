from itertools import product

def solution(users, emoticons):
    answer = []

    SaleRate = [10, 20, 30, 40]

    pros = list(product(SaleRate, repeat=len(emoticons)))

    max_sale = [0, 0]

    for pro in pros:
        sales = [0, 0]

        for user in users:
            purchase = 0

            for i in range (len(pro)):
                if user[0] <= pro[i]:
                    purchase += ((100-pro[i])*(emoticons[i]//100))

                if purchase >= user[1]:
                    sales[0] += 1
                    break
            else:
                sales[1] += purchase

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


