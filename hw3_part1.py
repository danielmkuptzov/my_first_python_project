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
    my_dict = {}
    with open(file_name) as f:
        for line in f:
            data = line.split()
            if(data[0] == "add"):
                if(data[1] == "product"):
                    product = ProductData.__init__(float(data[3]), float(data[4]))
                    my_dict[line[2]] == product
            if(data[0] == "change"):
                if(data[1] == "amount"):
                    element = my_dict[data[2]]
                    element.change_amount(float(data[3]))
            if(data[0] == "ship"):
                if(data[1] == "order"):
                    for i in range(2, data.__len__(), 2):
                        data = my_dict[data[i]]
                        data.sell_item(float(data[i+1]))
    return my_dict
def find_best_selling_product(file_name):
    shop_log = file_analize(file_name)
    