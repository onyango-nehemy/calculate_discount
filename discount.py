def calculate_discount(price,discount_percent):
    if(discount_percent>=20):
        final_price=price-(price*discount_percent/100)
        return final_price
    else:
        return price


price=float(input("enter the price:"))
discount_percent=float(input("enter discount percent:"))

result=calculate_discount(price,discount_percent)
print(f"final price: {result}")

