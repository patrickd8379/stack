class Stack:
    print("In stack")
    def __init__(self):
        print("In init")
        length = 3
        print("Past length")
        self.head = -1
        self.length = length
        self.stack = []
        for i in range(self.length):
            self.stack.append([])

    def push(self, item):
        if self.head + 1 == self.length:
            return "Stack is full"
        else:
            self.stack[self.head + 1] = item
            self.head += 1
            return self.stack, self.head

    def popIt(self):
        if self.head == -1:
            return "There is nothing to pop"
        else:
            outputValue = self.stack[self.head]
            self.stack[self.head] = []
            self.head -= 1
            return print(outputValue), self.stack, self.head

    def peek(self):
        return print(self.stack[self.head])


myStack = Stack()
print(myStack.push("1"))
print(myStack.stack)
print(myStack.push("2"))
print(myStack.stack)
print(myStack.push("3"))
print(myStack.stack)
print(myStack.push("4"))
print(myStack.stack)
print(myStack.popIt())
print(myStack.stack)
myStack.peek()
print(myStack.stack)
