class myList:
    def __init__(self,*arg) -> None:
        self.l1 = list(arg)
        
    def merge(self,*arg):
        ( self.l1.extend(arg))
    def sum (self):
        print((sum(self.l1)))
    def average(self):
        if len(self.l1)!= 0:
            print((sum(self.l1)/len(self.l1)))
        else:
            print(0)
    
l1 =  myList(2,3,4,5,6) #you might need a list inside your class to store the values
l1.sum()
l1.merge(4,5,9)
l1.sum()
l1.average()
print('-----------------------------')
l2 =  myList()
l2.average()
l2.merge(1,2,4,8)
l2.sum()
