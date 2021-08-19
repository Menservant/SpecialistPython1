# Дан словарь, содержащий данные о товаре из магазина
# "price" - цена товара в валюте "currency"
# "count" - количествотовара в магазине
# Считая,что курс доллара равен dollar_rate
# Вычислите цену всех товаров с названием "name" в долларах

item = {"name": "Кроссовки",
        "price": "7540.5",
        "currency": "rub",
        "count": "10"}
dollar_rate = 74.12
new_price = float(item.get("price"))
new_count = float(item.get("count"))
dollar_value = new_price*new_count/dollar_rate
print(dollar_value)
