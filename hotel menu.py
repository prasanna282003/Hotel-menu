menu={
    "dosa":50,
    "idli":40,
    "poori":30,
    "palav":35,
    "pongal":45,
    "coffee":20,
    "tea":10
}
print("Hello welcome to hotel shubam \n Here the menu for You")
print("""
    dosa:50
    idli:40
    poori:30
    palav:35
    pongal:60
    coffee:20
    tea:10
""")
item_total=0
item_1=input("please order the food : ")
if item_1 in menu:
    print("order confirmed")
    item_total+=menu[item_1]
    print(f"Amount for {item_1} is {item_total} Rs")
else:print(f"ordered item {item_1} is not available")
another_order=input("do you want to add one more item ( yes / no)")
if another_order=="yes":
    item_2=input("please order the food : ")
    if item_2 in menu:
      print("order confirmed")
      item_total+=menu[item_2]
      print(f"Amount for {item_2} is {menu[item_2]} Rs")
    else:print(f"ordered item{item_2} is not available")
else:print("ok then fine")
print(f"Your Total bill is {item_total} Rs \nThank You for visiting ! ")