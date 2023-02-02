#BigNumber
CodingTest에서 뒤큰수를 구하는 문제

![Picture1](https://user-images.githubusercontent.com/123911778/216243776-912cbd46-62e3-4173-b011-e8b038276465.png)
list의 뒤에 있는 큰 수 중 가장 가까이에 있는 수를 뒤큰수라고 한다.
각 항별로 뒤큰수를 출력하고 뒤큰수가 없으면 -1을 출력하는 프로그램이다.

예를 들어 Picture1에서 list [2, 3, 3, 5]는 2에서 바로 뒤의 큰 수는 3이고 3의 바로 뒤에 있는 큰수는 5, 
뒤에 있는 3의 바로 뒤의 큰 수는 5, 5는 가장 마지막에 있으므로 뒤큰수가 존재하지 않아 -1을 반환한다.

[9, 1, 5, 3, 6, 2]의 경우 9보다 큰 수가 없으므로 -1
1의 바로 뒤의 큰 수는 5, 5의 바로 뒤의 큰 수는 6, 3의 바로 뒤의 큰 수는 6,
6의 바로 뒤의 큰 수는 없고, 2는 마지막 숫자이므로 -1을 반환한다.

이 문제는 간단하게 이중 for문을 사용하여 풀 수 있다. 
<hr/>
for i in range(len(list)-1):
  for j in range(1, len(list)):
    if list[i] < list[j]:
      answer[i] = list[j]
      break
</hr>
