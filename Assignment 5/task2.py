class Shopidify:
    def __init__(self,name = None):
        self.name = "Guest" 
        self.cart = [] 
        self.p_his = None 
        if self.name == "Guest":
            print("Welcome to Shopidify")
        else:
            print(f"Welcome {self.name} to Sopidify")
            
    def add_to_cart(self, *arg):
        count = 0
        if type(arg[0])== list  :
            temp = ''
            for i in arg[0]:
                # temp = ''
                if type(i)==str:
                    # print(i)
                    temp += i 
                else:
                    # print(temp)
                    temp += ": " + str(i)+"x"
                count += 1 
                if count == 2 :
                    self.cart.append(temp)
                    temp = ""  
                    count = 0 
                
        if type(arg[0])== str and len(arg) == 1:
            temp = arg[0] + ": " + "1"+"x"
            if temp in self.cart:
                ind = self.cart.index(temp)
                temp2 = self.cart[ind][-2]
                temp = arg[0] + ": " + str(int(temp2)+1)+"x"
            self.cart.append(temp)
            # self.cart = set(self.cart)
            
            
        elif type(arg[0]) == str and type(arg[1] == int):
            temp = arg[0] + ": " + str(arg[1])+"x"
            print(temp)
            self.cart.append(temp)
            
    def display_cart(self):
        print(f"Items in the cart for {self.name}:")
        for i in self.cart :
            print(f"-{i}")
            
                
                    
        
    
guest_account = Shopidify()
print("1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account = Shopidify("John")
print("2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan", 2)
guest_account.add_to_cart("Luffy Action Figure")
guest_account.display_cart()
print("3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.add_to_cart(["Chocolate Chip Cookies", 3,"Goku Action Figure",2,"Dumbbells-5kg",2])
john_account.display_cart()
print("4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan")
guest_account.display_cart()
# print("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# guest_account.checkout()
# print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# guest_account.display_history()
# print("7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# john_account.checkout()
# print("8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# john_account.display_history()
# print("9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


tupe =([2,3])