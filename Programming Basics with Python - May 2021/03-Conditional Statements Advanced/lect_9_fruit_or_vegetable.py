product_name = str(input().lower())

if product_name == str('banana') or product_name == str('apple') or product_name == str(
        'cherry') or product_name == str('kiwi') or product_name == str('lemon') or product_name == str('grapes'):
    print('fruit')

elif product_name == str('tomato') or product_name == str('cucumber') or product_name == str(
        'pepper') or product_name == str('carrot'):
    print('vegetable')
else:
    print('unknown')
