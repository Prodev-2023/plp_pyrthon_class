
# calculator that calculates the percentage of discount on any product

def calculate_discount(price,discount_price):
    discount_price_percent = (price /100) * discount_price
    if discount_price_percent > 20 :
        return price - discount_price_percent
    else:
        return price
    
sales = calculate_discount

print(sales(200,10))