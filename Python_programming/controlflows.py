def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent/100))
        return discounted_price
    else:
        return price
    
price = int(input("Enter the price: "))
discount_percent = int(input("Enter the discount: "))
print ("The discounted price is:", calculate_discount(price, discount_percent))
