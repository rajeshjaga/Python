class Stack:
    def __init__(self, size):
        self.stk, self.len, self.top = [], size, -1

    def is_empty(self):
        if self.top == -1:
            return True

    def is_full(self):
        if self.top == self.len - 1:
            return True

    def Stck_push(self, ele):

        self.top += 1
        self.stk.append(ele)
        print(f"Ele {ele} is inserted")

    def stck_pop(self):
        print(f"{self.stk[self.top]} deleted")
        self.stk.pop(self.top)
        self.top -= 1

    def stck_display(self):
        print(self.stk)


print("Implementing stack in Python\n")
s = Stack(int(input("Enter the size of the stack")))

while True:
    print("1.push \n 2.pop \n 3.display")
    ch = int(input("chose the stack op to perform"))
    if ch == 1:
        if s.is_full():
            print("stack is full")
        else:
            s.Stck_push(int(input("enter the element values")))
    elif ch == 2:
        if s.is_empty():
            print("stack underflow")
        else:
            s.stck_pop()
    elif ch == 3:
        if s.is_empty():
            print("Stack underflow")
        else:
            s.stck_display()
    else:
        break
