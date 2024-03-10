a = input().split()
a = list(map(int,a))
revs = ''
digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
          "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
          "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
          "U", "V", "W", "X", "Y", "Z")
if a[1] == 10:
    print(a[0])
else:
    while a[0] > 0:
        a[0], mod = divmod(a[0], a[1])
        revs = digits[mod] + revs
       
    print(revs)
