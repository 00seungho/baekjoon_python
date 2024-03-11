import sys
class Stack():
    def __init__(self):
        self.a = []
    def insert(self, x):
        self.a.append(x)
    def pop_stack(self):
        return self.a.pop() if self.a else -1
newStack = Stack()
K = int(sys.stdin.readline())
for _ in range(K):
    select = int(sys.stdin.readline())
    if select == 0:
        newStack.pop_stack()
    else:
        newStack.insert(select)
print(sum(newStack.a))