class Order:

    @staticmethod
    def calculate_tax(amount, tax_rate):
        return amount * (tax_rate / 100)
    
print(Order.calculate_tax(1000, 18))