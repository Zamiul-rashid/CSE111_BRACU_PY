class Smartphone:
    def __init__(self,name  = None) -> None:
        self.name = name 
        self.feature = []
        
    def setName(self, name ):
        self.name = name 
    
    def addFeature(self,f1,f2):
        if self.name == None :
            print(F"Feature can not be added without phone name")
        else:
            self.feature.append((f1,f2))
            
    def printDetail(self):
        print(f"Phone Name: {self.name}")
        for i in self.feature:
            print(f"{i[0]}: {i[1]}")

s1 = Smartphone()
print("=================================")
s1.addFeature('Display', '6.1 inch')
print("=================================")
s1.setName('Samsung Note 20')
s1.addFeature('Display', '6.1 inch')
s1.printDetail()
print("=================================")
s2 = Smartphone('Iphone 12 Pro')
s2.addFeature('Display', '6.2 inch')
s2.addFeature('Ram', '6 GB')
print("=================================")
s2.printDetail()
s2.addFeature('Display', 'Amoled panel')
s2.addFeature('Ram', 'DDR5')
print("=================================")
s2.printDetail()
print("=================================")

print(s2.feature)