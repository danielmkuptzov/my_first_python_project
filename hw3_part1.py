class ProductData:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price
        self.profit=0
    def change_amount(self, amount):
        self.amount += amount
    def sell_item(self, amount):
        if(self.amount < amount):
            return
        self.change_amount(-amount)
        self.profit = self.price * amount
def file_analize(file_name):
    with open(file_name) as f:
        line = f.readline()
        while line:
            data = line.split()
