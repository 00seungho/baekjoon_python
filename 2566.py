Matrix =[]
for i in range(9):
    line = list(input().split())
    line = list(map(int,line))
    Matrix.append(line)

max = 0
idxcol = 0
idxrow = 0
for i in range(9):
    for j in range(9):
        if max < Matrix[i][j]:
            max = Matrix[i][j]
            idxcol = i
            idxrow = j

print(max)
print(f"{idxcol+1} {idxrow+1}")