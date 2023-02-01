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
