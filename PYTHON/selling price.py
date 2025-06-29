cost_price=int(input("enter cost price"))
discount=int(input("enter the discount"))
discount_amount=(discount/100)*cost_price
selling_price=cost_price-discount_amount
print("selling price=",selling_price)