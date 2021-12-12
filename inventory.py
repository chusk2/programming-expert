class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.inventory = {}
        self.current_quantity = 0

    def add_item(self, name, price, quantity):
        # create conditions to be fullfilled as requisites to add item
        not_exists = name not in self.inventory.keys()
        enough_room = (quantity + self.current_quantity) <= self.max_capacity
        if not_exists and enough_room:
            self.inventory[name] = {}
            self.inventory[name]['price'] = price
            self.inventory[name]['quantity'] = quantity
            self.current_quantity += quantity
            return True
        return False

    def delete_item(self, name):
        if name in self.inventory.keys():
            item_quantity = self.inventory[name]['quantity']
            self.inventory.pop(name)
            # reclaim the room left by the eliminated item in inventory
            self.current_quantity -= item_quantity
            return True
        return False

    def get_items_in_price_range(self, min_price, max_price):
        # self.inventory.items() returns tuple: (item, dic(price, quantity))
        # i[0] = key ('name')
        # i[1] = value (dict(´quantity`,'price'))
        items_within_price_range = [i[0] for i in self.inventory.items()
                                    if  min_price <= i[1]['price'] <= max_price]
        return items_within_price_range

    def get_most_stocked_item(self):
        if not self.inventory:  # empty inventory
            return None
        quantities = sorted(self.inventory.items(),
                            key = lambda item : item[1]['quantity'])
        return quantities[-1][0]
