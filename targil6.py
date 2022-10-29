from time import sleep
from random import randint
from datetime import datetime
'''
today = date.today()
print("Today's date:", today)

d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

תרגיל שני
הזמן והתאריך המדויק של היום
now = datetime.now()
print(now)
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
print("date and time =", dt_string)

תרגיל שלישי
מקבל שם ושם משפחה מחליף את האותיות בכל מילה ומחליף בין השם משפחה לשם בסדר 
full_name = input("enter name and last name : ").split()
full_name[0] = full_name[0][::-1]
full_name[1] = full_name[1][::-1]
str_fullname = full_name[0] + " " + full_name[1]
print(str_fullname)
 
 תרגיל רביע
 מפצל את הקובץ
url = input("enter URL : ").split(".")
print(url[1])



'''
'''
num = 22.123456
tmp = 4
num = f"%.{tmp}f" % num
print(num)
'''
'''
'''
'''
my_dict = {"dan": "nudelman","max": "pass"}
print(my_dict)
מוסיף מפתח וערך חדשים למילון
my_dict.update({"david": "suckner"})
מעדכן לפי המפתח אם לא נמצא מוסיף חדש
my_dict["david"] = "mertal"
print(my_dict)
print("dan" in my_dict.values())
'''
'''
for x in range(2,20,2):
    print(x)
'''
'''
for x in range(5):
    name = input("enter your name : ")
    age = int(input("enter your age : "))
    phone = int(input("enter your phone : "))
'''
'''
num = int(input("enter num : "))
num2 = num * 11
num3 = num * 111
print(f"new num {num + num2 + num3}")
'''
'''
dict = {0: 10, 1: 20}
dict.update({2:22})
print(dict)
'''
'''
dict = {}
string = input("enter string : ")
num = 1
for x in string:
    dict.update({x:num})
    num = num + 1
print(dict)
'''
'''
string = input("enter string : ")
char_again = []
char2 = []
num = 1
count_list = []
for x in string:
    char_again.append(x)
for x in char_again:
    count = 0
    for i in string:
        if i == x:
           count += 1
           char2.append(count)
    count_list.append(count)

new_dict = {}
for x in range(len(count_list)):
    new_dict.update({char_again[x]:count_list[x]})
print(new_dict)
'''
'''
list = []
while len(list) < 5:
    list.append((input("enter number : ")))

count = 0
for x in list:
    count += int(x)
print(count)
'''
'''
list = ["this","flow","dada","mama","this","this"]
list.pop(0)
list.pop(3)
list.pop(3)

print(list)
'''
'''
srtring = input("enter string pleas : ")
repeted_list = []
count_list = []
tmp_list = []

for x in srtring:
    repeted_list.append(x)
cont = 0
is_in_list = False
print(repeted_list)
for x in range(int(len(srtring))):
    cont = 1
    for i in repeted_list:
        if srtring[x] not in tmp_list:
           tmp_list.append(srtring[x])
           continue
        if srtring[x] == i and cont == 1:
            cont += 1
            print("second")
            count_list.append(f"{srtring[x]} : {cont}")
        elif srtring[x] == i and cont > 1:
            cont += 1
            print("more than 2 ")
            count_list.append(f"{srtring[x]} : {cont}")
print(f"{tmp_list} \n {count_list}")
'''
'''
num = int(input("enter num :"))
if num % 2 == 0:
    print("even")
else:
    print("not even")
'''
'''
height = float(input("enter you height in feet"))
new_height = height * 30.48
print(f" your height is {new_height} in cm")
'''
list = [1,2,3]
list = type(list)()
print(type(list)())

