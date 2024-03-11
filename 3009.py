first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
foth = []
if first[0] == second[0]:
    foth.append(third[0])
elif second[0] == third[0]:
    foth.append(first[0])
elif first[0] == third[0]:
    foth.append(second[0])

if first[1] == second[1]:
    foth.append(third[1])
elif second[1] == third[1]:
    foth.append(first[1])
elif first[1] == third[1]:
    foth.append(second[1])

print(f"{foth[0]} {foth[1]}")