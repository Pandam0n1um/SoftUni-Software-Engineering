statistics={}
while True:
    elements = input()
    if elements == "statistics":
        break
    product, quantity = elements.split(": ")
    if product in statistics:
        statistics[product]+=int(quantity)
    else:
        statistics[product]=int(quantity)

result="Products in stock:"
total_quantity=0
total_products=0
for key,val in statistics.items():
    result+=f"\n- {key}: {val}"
    total_products+=1
    total_quantity+=val

result+=f"\nTotal Products: {total_products}\nTotal Quantity: {total_quantity}"
print(result)