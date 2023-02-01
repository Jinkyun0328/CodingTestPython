from math import gcd

def solution(nums1, nums2):
    gcd1, gcd2 = nums1[0], numb2[0]
    for each1, each2 in zip(nums1[1:], nums2[1:]):
        gcd1, gcd2 = gcd(each1, gcd1), gcd(each2, gcd2)

    answer = []
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

    return max(answer) if answer else 0
