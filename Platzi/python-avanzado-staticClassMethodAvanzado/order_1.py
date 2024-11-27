class Order:
    global_discount = 10

    def __init__(self,amount):
        self.amount = amount

    @classmethod
    def update_gloabal_discount(cls, new_discount):
        cls.global_discount = new_discount

Order.update_gloabal_discount(15)
print(Order.global_discount)
        
        
