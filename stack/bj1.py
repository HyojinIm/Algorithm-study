import sys

class myStack:
    def __init__(self):
        self.stack = []
    def push(self, num):
        self.stack.append(num)
    def pop(self):
        if self.stack:
            return self.stack.pop(len(self.stack)-1)
        else:
            return -1
    def size(self):
        return len(self.stack)
    def empty(self):
        if self.stack:
            return 0
        else:
            return 1
    def top(self):
        if self.stack:
            return self.stack[len(self.stack)-1]
        else:
            return -1

a = myStack()

num = sys.stdin.readline().rstrip()
for i in range(int(num)):
    temp = sys.stdin.readline().rstrip()
    if(temp[:4] == "push"):
        a.push(int(temp[5:]))
    elif(temp == "pop"):
        print(a.pop())
    elif(temp == "size"):
        print(a.size())
    elif(temp == "empty"):
        print(a.empty())
    elif(temp == "top"):
        print(a.top())