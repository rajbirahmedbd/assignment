mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Russia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchange_rate': 107.25
            }
def usd_to_bdt(usd,exchange_rate):
    """
    This function will convert from usd to bdt
    :param usd: usd price of the product
    :param exchange_rate: exchange rate from usd to bdt
    :return: product price in BDT
    """
    usd = float(usd.strip(' USD'))
    bdt = usd * exchange_rate
    return bdt

for m in mobile_data['data']:
    usd = m['price']
    bdt = usd_to_bdt(usd,mobile_data['exchange_rate'])
    name = m['name']
    country = m['made']
    print(f'{name} is made in {country}. The price is {usd} which is almost equal to {int(bdt)} BDT')