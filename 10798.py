Matrix =[]
for i in range(5):
    line = input()
    if len(line) < 15:
        line += ' ' * (15 - len(line))
    Matrix.append(line)

for i in range(15):
    for j in range(5):
        if Matrix[j][i] == ' ':
            continue
        print(Matrix[j][i],end='')