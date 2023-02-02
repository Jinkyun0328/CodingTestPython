# Connected_One
2차원 matrix인 canvas에서 1을 찾은 후 연결된 1을 같은 숫자로 변경하는 프로그램
응용 : 코딩테스트 무인도

## Python file
FILL.py
재귀함수를 사용하여 구현

FILL_Comment.py
주석 첨부

NRFILL.py
재귀함수를 사용하지 않고 stack을 사용하여 구현

NRFILL_Comment.py
주석 첨부

## Algorithm
![picture1](https://user-images.githubusercontent.com/123911778/216236471-9fe8dce0-3662-4315-95da-77a307ff7c7e.png)

0과 1이 채워져 있는 2차원 배열에서 서로 연결되어 있는 1을 다른 숫자로 채워넣는 프로그램이다.
[picture1]에서 위의 matrix을 넣고 프로그램을 돌리면 아래 matrix을 출력한다.
상하좌우로 연결되어 있는 1의 집합은 총 4개가 나오고 각각 2, 3, 4, 5로 변경된 것을 볼 수 있다.

- 행렬에서 1의 위치를 찾는다.
- 1이 있는 좌표를 기준으로 8가지 방향에 있는 좌표에 있는 숫자가 1인지 확인한다.
- 1이 있으면 같은 숫자로 채운다.
- 연결되어 있다는 것은 1번 좌표에서 오른쪽 위로 간 다음 거기서 다시 8가지 방향을 확인하고 다시 이동한 다음 확인하는 식으로
- 재귀함수와 stack을 사용하여 구현할 수 있다.

![picture2]([https://user-images.githubusercontent.com/123911778/216236471-9fe8dce0-3662-4315-95da-77a307ff7c7e.png](https://user-images.githubusercontent.com/123911778/216238271-ed7f94c6-46fe-4a0d-ba5d-99547d3a1b22.png)
- matrix에서 1을 찾는다.
- 8가지 방향에 대해서 1이 있는지 확인한다.
- 1이 아니라면 다른 방향을 살핀다.
- 1이 있다면 현재 좌표를 stack에 저장한 후 1이 있는 위치로 이동하고 8가지 방향에서 1이 있는지 확인한다.

![picture3]([[https://user-images.githubusercontent.com/123911778/216236471-9fe8dce0-3662-4315-95da-77a307ff7c7e.png](https://user-images.githubusercontent.com/123911778/216238271-ed7f94c6-46fe-4a0d-ba5d-99547d3a1b22.png](https://user-images.githubusercontent.com/123911778/216238274-6b8ffe74-69f1-42df-8d24-926edb64584a.png))
첫 번째 1의 모임은 위의 방향으로 이동하면서 2로 바뀌게 된다.

