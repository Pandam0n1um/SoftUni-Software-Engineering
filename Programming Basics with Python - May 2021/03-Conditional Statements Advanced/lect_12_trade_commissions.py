city_name = str(input().lower())

trade_volume = float(input())

trade_volume_check = None

city_name_check = None

trade_commission = 0

if city_name == str('sofia'):
    if 0 <= trade_volume <= 500:
        trade_commission = (trade_volume*0.05)
    elif 500 < trade_volume <= 1000:
        trade_commission = (trade_volume * 0.07)
    elif 1000 < trade_volume <= 10000:
        trade_commission = (trade_volume * 0.08)
    elif 10000 < trade_volume:
        trade_commission = (trade_volume * 0.12)
    else:
        trade_volume_check=0

elif city_name == str('plovdiv'):
    if 0 <= trade_volume <= 500:
        trade_commission = (trade_volume*0.055)
    elif 500 < trade_volume <= 1000:
        trade_commission = (trade_volume * 0.08)
    elif 1000 < trade_volume <= 10000:
        trade_commission = (trade_volume * 0.12)
    elif 10000 < trade_volume:
        trade_commission = (trade_volume * 0.145)
    else:
        trade_volume_check=0

elif city_name == str('varna'):
    if 0 <= trade_volume <= 500:
        trade_commission = (trade_volume*0.045)
    elif 500 < trade_volume <= 1000:
        trade_commission = (trade_volume * 0.075)
    elif 1000 < trade_volume <= 10000:
        trade_commission = (trade_volume * 0.10)
    elif 10000 < trade_volume:
        trade_commission = (trade_volume * 0.13)
    else:
        trade_volume_check=0
else:
    city_name_check = 0

if trade_volume_check==0 or city_name_check==0:
    print('error')
else:
    print(f'{trade_commission:.2f}')