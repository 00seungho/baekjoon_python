import sys
class Stack():
    def __init__(self):
        self.a = []
    def insert(self, x):
        self.a.append(x)

    def pop_stack(self):
        return self.a.pop() if self.a else -1

    def stack_length(self):
        return len(self.a)

    def is_empty(self):
        return int(not self.a)

    def print_top(self):
        return self.a[-1] if self.a else -1
newStack = Stack()
N = int(sys.stdin.readline())
for _ in range(N):
    select = sys.stdin.readline().split()
    if select[0] == "1":
        newStack.insert(int(select[1]))
    else:
        if select[0] == "2":
            print(newStack.pop_stack())
        elif select[0] == "3":
            print(newStack.stack_length())
        elif select[0] == "4":
            print(newStack.is_empty())
        elif select[0] == "5":
            print(newStack.print_top())
