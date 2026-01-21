
print("WELCOME TO OUR RESTAURANT")
menue={
    "coffee":560,
    "cappichino": 490,
    "lattee tea":380,
    "oreo shake":980,
    "mint margritta":789,
    "pizza":1090
}

print("coffee: rs560\n cappichino: rs490\n lattee tea: rs380\n" \
" oreo shake:rs 980\n mint marrgritta: rs789\n pizza:rs1090")

order_total=0

your_cart=[]

item_1=(input("enter what_you_need"))

if item_1  in menue:
      order_total += menue[item_1]
      print(f"{item_1} has been added to your cart ")
      your_cart.append(item_1)
    
else:
   print("This item is not available")

another_order=input("do you want something more")
if another_order =="yes":
 
   item_2= input("enter the name of second item")
   if item_2  in menue:
      order_total += menue[item_2]
      print(f"{item_2} has been added to your cart ")
      your_cart.append(item_2)
   else:
     print("This item is not available")

print(your_cart)

print(f"the total amount is{order_total}")

print("THANKS for visiting us")