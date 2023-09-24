from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    gcdA, gcdB = reduce(gcd, arrayA), reduce(gcd, arrayB)
   
    answer = []
    
    if all(each % gcdB for each in arrayA):
        answer.append(gcdB)
    if all(each % gcdA for each in arrayB):
        answer.append(gcdA)
            
    return max(answer) if answer else 0

# python의 내장함수 all()은 리스트에 담겨 있는 요소들이
# 모두 boolean으로 변환했을 때 True인지를 확인하는 함수이다.
# 반복문으로 순회할 수 있는 모든 객체를 인자로 받을 수 있기 때문에
# 반복문 없이 리스트가 모두 참인지 확인할 수 있다.
# all([1, "TEST", 1 < 2, 2 + 3 == 5]) # True
# all([0, "", {}, [], None, 1 > 2, 2 + 3 == 4]) # False
# False에 해당하는 인자를 하나라도 포함하고 있으면 False을 반환한다.
# 위에서는 arrayA에 있는 인자 중 하나라도 gcdB로 나누어 떨어지면 False을 반환한다.

# python의 functools 내장 모듈의 reduce() 함수는 여러 개의 데이터를 대상으로
# 주로 누적 집계를 내기 위해서 사용한다.
# reduce(집계 함수, 순회 가능한 데이터[, 초기값])
# 여기서는 gcd 함수를 집계 함수로 사용하여 arrayA와 arrayB의 최대공약수를 구했다.
