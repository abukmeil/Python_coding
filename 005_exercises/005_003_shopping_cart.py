################################### Calculate the area of a rectangle #########################

item        =   input("What item would you to buy?: ")
price       =   float(input("What is the price?: "))
quantity    =   int(input("How many would you like?: "))

total= price*quantity
print(f"You have bought {quantity} x {item}")
print(f"Your total is: ${total}")
print()
'Rounding the total number'
print(f"Your total is: ${round(total,2)}")

