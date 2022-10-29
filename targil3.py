"""""""""
יצירת רשימה
new_list = ["dan","nudelman"]

הוספת תא עם ערך נוסף לרשימה חדשה
new_list2 = new_list + ["27"]

print(new_list2)
הסרה של ערך ספציפי בתא שבתוך הרשימה כש אני יודע מראש את הערך שלו
new_list2.remove("27")

print(f"name : {new_list2[0]}")
print(f"last name : {new_list2[1]}")

מבקש מהמשתמש את הגיל שלו לצורך הוספה לתא חדש ברשימה מסוג אינט
new_list2.append(int(input("what is your age ? : ")))
print(new_list2)
print(f"your age is : {new_list2[2]}")
"""""""""
"""""""""
name_list = list(input("your name is ? :"))
print(f"here is a a list of the chars in your name with your name \n{name_list}")
"""""""""
"""""""""
my_list = []
my_list2 = []
string = "dan nudelman"
string2 = "dan nudelman\nhow are you ?"

יצירת רשימה חדשה שכל תא מחלוק לפי הרווח בערך של הסטרינג
my_list = string.split()
יצירת רשימה חדשה שכל תא מחלוק לפי השורה החדשה בערך של הסטרינג
my_list2 = string2.splitlines()
print(my_list)
print(my_list2)
מדפיס את מספר התאים ברשימה
print(len(my_list2))

my_list = []

הוספת תא חדש עם ערך בתוך לרשימה הקיימת
my_list.append("dan")
print(my_list)

"""""""""
"""""""""
my_list = []
my_list.append(("name: " + input("what is your name ? :")).split())
my_list.append(("last_name: " + input("what is your name ? :")).split())
my_list.append(("age: " + input("what is your age ? : ")).split())
print(my_list)
my_list[0].pop(0)
my_list[0].insert(0,"name : ")
my_list[1].pop(0)
my_list[1].insert(0,"last name : ")
print(my_list)
print("last name : " in my_list)
"""""""""
"""""""""
name_list = ["dan","david","michael","antone","itzik","max"]
score = [272,425,6625,1126,225,3335]
if input("what is your name ? :  ") in name_list:
    print("welcome !")
else:
    print("sorry your not in the name list !")
"""""""""
"""""""""
contact_list = input("enter your name,age,mail,phone-number and separate theme by ',' ").split(",")
print(f"your name is : {contact_list[0]}\nyour age : {contact_list[1]}\nyour mail : {contact_list[2]}\nyour phone number : {contact_list[3]}")
"""""""""
"""""""""
print("------------------------")
ip_list = ["1.1.1.1","2.2.2.2"]
print(ip_list)
ip_list.append("3.3.3.3")
ip_list.append("4.4.4.4")
ip_list.append("5.5.5.5")
print(ip_list)
ip_list.pop(2)
print(ip_list)
print(f"Ip List is : {ip_list}")
print(f"Ip List length is : {len(ip_list)}")
"""""""""


