
class ProductData:
    def __init__(self, amount, price):
        self.amount = float(amount)
        self.price = float(price)
        self.profit = 0

    def change_amount(self, amount):
        self.amount += float(amount)

    def sell_item(self, amount_):
        amount = float(amount_)
        if(self.amount < amount):
            return
        self.change_amount(-amount)
        self.profit += self.price * amount


def file_analize(file_name):
    products = {}

    with open(file_name) as f:
        for line in f:
            splitted = line.split()
            command = " ".join(splitted[:2])
            key = splitted[2]

            if command == "add product":
                products[key] = ProductData(product, splitted[3], splitted[4])

            elif command == "change amount":
                products[key].change_amount(splitted[3])

            elif command == "ship order":
                for i in range(2, len(splitted), 2):
                    products[splited[i]].sell_item(splitted[i+1])

    return products


def find_best_selling_product(file_name):
    shop_log = file_analize(file_name)
    most_expensive = 0
    most_profitble_name=""

    for name, product in enumerate(shop_log):
        if most_expensive < product.profit:
            most_expensive = product.profit
            current_selling_price = product.price
            most_profitble_name=name
        elif most_expensive == product.profit \
                and most_profitble_name > name:
            most_profitble_name=name
            current_selling_price = product.price

    return most_profitble_name, current_selling_price


def find_k_most_expensive_products(file_name, k):
    if k <= 0:
        return []
    ordered = sorted(file_analyze(file_name).items(), key=lambda pair: (pair[1].price, pair[0]))