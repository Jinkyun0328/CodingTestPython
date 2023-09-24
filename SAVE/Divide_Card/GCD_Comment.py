# math mudule에서 gcd 함수를 import 한다.
from math import gcd

def solution(nums1, nums2):
    # nums1과 nums2의 최대공약수를 gcd1, gcd2에 저장한다.
    gcd1, gcd2 = nums1[0], numb2[0]
    for each1, each2 in zip(nums1[1:], nums2[1:]):
        gcd1, gcd2 = gcd(each1, gcd1), gcd(each2, gcd2)

    answer = []

    # nums1중 하나라도 gcd2로 나누어 떨어지면 반복문을 종료한다.
    # for else문은 for문이 중간에 break로 끝나지 않고 끝까지
    # 수행했을 때 else문을 수행한다.
    # 모두 나누어 떨어지지 않으면 answer에 gcd2을 넣는다.
    for each1 in nums1:
        if each1 % gcd2 == 0:
            break
    else:
        answer.append(gcd2)


    for each2 in nums2:
        if each2 % gcd1 == 0:
            break

    else:
        answer.append(gcd1)

    # answer이 비어있으면 0을 반환
    # answer에 값이 있으면 최댓값을 반환한다.
    return max(answer) if answer else 0
