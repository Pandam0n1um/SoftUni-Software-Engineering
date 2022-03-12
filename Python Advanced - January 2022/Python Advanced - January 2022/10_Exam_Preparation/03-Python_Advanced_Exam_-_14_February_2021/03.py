def stock_availability(inventory, action, *args):
    if action == 'delivery':
        inventory.extend(list(args))
    elif action == 'sell':
        if not args:
            inventory = inventory[1:]
        elif isinstance(args[0], int):
            inventory = inventory[args[0]:]
        else:
            for elem in args:
                if elem in inventory:
                    inventory=[x for x in inventory if not x==elem]
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
