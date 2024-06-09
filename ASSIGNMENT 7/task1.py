class KK_tea:
    sales = {};count  = 0
    def __init__(self, Price,N_pac = 50) -> None:
        self.name = "KK Regular Tea"
        self.price = Price
        self.N_pac = N_pac
        self.sold = False
        self.weight = self.N_pac * 2
        KK_tea.sales[self.name] = KK_tea.sales.get(self.name, 0) 
        

    def product_detail(self):
        print(f"Name: {self.name}, Weight: {self.weight} \
            \nTea Bags: {self.N_pac}, Price: {self.price} \nStatus: {self.sold}")

    
        
    @classmethod
    def update_sold_status_regular(cls,*args):
        for i in args:
            cls.sales[i.name] = cls.sales.get(i.name, 0) + 1
            cls.count += 1 
            i.sold = True
    @classmethod
    def total_sales(cls):
            print(f"Total sales: {cls.sales}")
class KK_flavoured_tea (KK_tea):
    def __init__(self, flavour, price, N_tea) -> None:
        super().__init__(price, N_tea)
        self.name = flavour
    
    @classmethod    
    def update_sold_status_flavoured(cls, *args):
        for i in args:
            cls.sales[i.name] = cls.sales.get(i.name, 0) + 1    
            i.sold = True
            
        
t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()
