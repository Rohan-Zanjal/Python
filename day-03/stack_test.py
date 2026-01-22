#Implementation (using list)
class stack:
    def __init__(self):
        self.s = [] # initialize an empty stack

    def length(self):
        return len(self.s) # return the length of the stack
    
    def push(self,value):
        self.s.append(value) # push value onto the stack

    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is empty") # raise exception if stack is empty
        else:
            return self.s[0] # return the top value of the stack without removing it
        
    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is empty") # raise exception if stack is empty
        else:
            return self.s.pop() # remove and return the top value of the stack
        
    def display(self):
        print(self.s) # display the stack
        
stk = stack() # create an object of stack
stk.push(10) # push 10 onto the stack
stk.push(20) # push 20 onto the stack
stk.push(30) # push 30 onto the stack
stk.push(40) # push 40 onto the stack
stk.display() # display the stack


print(stk.pop()) # pop the top value of the stack
print(stk.pop()) # pop the top value of the stack
stk.display() # display the stack
print("The length of stack is :",stk.length()) # print the length of the stack

