'''
tomato_price = float(input("price of tomato : "))
orange_price = float(input("price of orange : "))
cola_price = float(input("price of cola : "))
chicken_price = float(input("price of chicken : "))
without_tax = tomato_price + orange_price + cola_price + chicken_price
tax = float("%.3f" % (without_tax * 0.17))
total = tax + without_tax

print(f"without tax : {int(without_tax)} \ntax price : {tax} \ntotal bill : {total}")
'''

'''
num = 3.445
num = "%.10f" % num
print("num = {}".format(num))
'''


name = "milman"
email = "justdan@walla.co.il"
age = 28
answer = name in "dniel"
print(f"your age : {age*3}\nyour name: {name[::-1]}\n{answer}")
