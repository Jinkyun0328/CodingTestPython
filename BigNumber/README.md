# BigNumber
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
<pre>
  <code>
    for i in range(len(list)-1):
      for j in range(1, len(list)):
        if list[i] < list[j]:
          answer[i] = list[j]
          break
  </code>
</pre>  

단, list의 크기가 길어질수록 소요시간은 n^2로 증가하기 때문에 처리속도가 늦어진다.
![Picture2](https://user-images.githubusercontent.com/123911778/216243779-1630d9c9-b1b8-419a-a3a6-4e66c05ec576.png)
이중 for문을 사용하여 구현했을 때 Picture2와 같이 시간초과가 나왔고 속도를 줄이기 위해서는 이중 for문 대신 stack을 사용해야 했다.

## Algorithm
- Numbers[i]가 바로 앞의 수보다 작으면 index을 stack에 push한다.
- Numbers[i]가 바로 앞의 수보다 크면 stack의 top()보다 큰 수인지 확인한다. (Numbers[i] > Numbers[stack.top()])
- Numbers[i]가 stack에 저장된 index의 숫자보다 작아질 때까지 반복문을 수행하며 stack을 pop하고 answer[pop()]에 Numbers[i]를 저장한다.
- stack에서 pop()한 index의 Numbers보다 작아지면 i를 push하고 다음으로 넘어간다.
- i for문이 끝나면 stack에 남은 수를 모두 pop하여 -1을 저장한다.

바로 뒤에 있는 큰 수 이기 때문에 stack의 안쪽에는 top보다 작은 Numbers의 index는 저장되어 있지 않기 때문에
이중 for문 대신 stack을 사용하여 처리속도를 빠르게 할 수 있었다.
