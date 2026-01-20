#Implement UNDO & REDO using Python Function .
#GFG POTD. 
class Solution:
    def __init__(self):
        self.document=[]
        self.stack=[]
    def append(self, x):
        self.document.append(x)
        self.stack.clear()

    def undo(self):
        self.stack.append(self.document.pop())

    def redo(self):
        self.document.append(self.stack.pop())

    def read(self):
        return "".join(self.document)
