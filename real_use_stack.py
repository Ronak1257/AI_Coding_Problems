# Implement the Stack Algorithm for any Real Time Use Case (no library use)

# using stack we can implement copy paste in the computer this is best solution we can do

class Real_Stack:
    def __init__(self):
        self.items=[""]*100
        self.top=-1

    def is_empty(self):
        return self.top==-1

    def push(self,data):
        self.top+=1
        self.items[self.top]=data
        print("Add in Clipboard : ",data)

    def pop(self):
        if not (self.is_empty()):
            print("Remove from Clipboard : ",self.items[self.top])
            self.top-=1
    def paste(self):
        if not (self.is_empty()):
            print("Pasted data : ",self.items[self.top])

Stack=Real_Stack()
inp=4
while(inp):
    inp=int(input("Enter number : 1) push 2) pop 3) paste 0) exit : "))
    match inp:
        case 1:
            da=input("Enter String : ")
            Stack.push(da)
        case 2:
            Stack.pop()
        case 3:
            Stack.paste()
            


            

