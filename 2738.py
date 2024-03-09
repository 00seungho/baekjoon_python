input_str = input()
NM = list(map(int, input_str.split()))

matrix1 = []
matrix2 = []

for i in range(NM[0]):
    numbers = input().split()
    row = [int(num) for num in numbers]
    matrix1.append(row)

for i in range(NM[0]):
    numbers = input().split()
    row = [int(num) for num in numbers]
    matrix2.append(row)

newMatrix = []
for i in range(NM[0]):
    new_row = [matrix1[i][j] + matrix2[i][j] for j in range(NM[1])]
    newMatrix.append(new_row)

for row in newMatrix:
    print(" ".join(map(str, row)))
