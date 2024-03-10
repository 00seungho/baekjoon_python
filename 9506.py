while True:
    a = int(input())
    if a == -1:
        break
    measure = []
    sum = 0
    for i in range(1, a + 1):
        if a % i == 0:
            measure.append(i)
    
    for i in range(len(measure)-1):
        sum += measure[i]
    if sum==a:
        print(f"{a} = ", end='')
        for i in range(len(measure)-1):
            if i < len(measure) - 2:
                print(f"{measure[i]} + ", end='')
            else:
                print(f"{measure[i]}", end='')
        print()
    else:
        print(f"{a} is NOT perfect.")
    