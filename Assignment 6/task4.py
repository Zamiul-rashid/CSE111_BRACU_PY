class NikeBD:
    branches = []
    sold = 0 

    def __init__(self, loc):
        self.loc = loc
        self.products_stock = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
        self.total_sold = 0
        NikeBD.branches.append(self)

    @classmethod
    def status(cls):
        print("Nike Bangladesh Status:")
        print(f"Branches Opened: {[branch.loc for branch in cls.branches]}")
        print("Currently Stocked")
        print(cls.total_stock())
        print(f"Sold: {cls.sold}")
        

    def details(self):
        print(f"Nike {self.loc} outlet:")
        print("Products Currently Stocked: ")
        print(self.products_stock)
        print(f"Sold: {self.total_sold}")

    def restockProducts(self, restock_dict):
        for product, quantity in restock_dict.items():
            if product in self.products_stock:
                self.products_stock[product] += quantity

    def productSold(self, sold_dict):
        for product, quantity in sold_dict.items():
            if product in self.products_stock and self.products_stock[product] >= quantity:
                self.products_stock[product] -= quantity
                self.total_sold += quantity
                self.__class__.sold += quantity

    @classmethod
    def total_stock(cls):
        total_stock = {}
        for product in ['Air Jordan', 'Cortez', 'Zoom Kobe']:
            total_quantity = sum(branch.products_stock[product] for branch in cls.branches)
            total_stock[product] = total_quantity
        return total_stock


# Driver Code
print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBD.status()
dhaka = NikeBD("Dhaka Banani")
chittagong = NikeBD("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts({"Air Jordan": 1200, "Cortez": 200, "Zoom Kobe": 200})
chittagong.restockProducts({"Air Jordan": 1000, "Cortez": 250, "Zoom Kobe": 100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBD.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan": 760, "Cortez": 90})
chittagong.productSold({"Air Jordan": 520, "Zoom Kobe": 70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBD.status()
