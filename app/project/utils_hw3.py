class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name: str, price: float, quantity: int):
        item_found = False

        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] = item['quantity'] + quantity
                item['price'] = price
                item_found = True

        if not item_found:
            new_item = {
                'name': item_name,
                'price': price,
                'quantity': quantity,
            }
            self.items.append(new_item)

    def remove_item(self, item_name: str):
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)
                break

    def get_total(self):
        total_price = 0

        for item in self.items:
            total_price += item['price'] * item['quantity']
        return total_price
