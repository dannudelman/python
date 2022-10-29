##dictionary
'''
מילון עם אתר וכתובת IP משויכת לו
my_dict = {"www.facebook.com": "8.8.8.8","www.youtube.com":["8.8.8.8","5.5.5.5"]}
print(my_dict)
'''
'''
my_dict = {"www.facebook.com": "8.8.8.8","www.youtube.com":["8.8.8.8","5.5.5.5"]}
להוסיף ערך חדש למילון
my_dict.update({"www.gmail.com":"9.9.9.9"})
print(my_dict)
'''
'''
my_dict = {"www.facebook.com": "8.8.8.8","www.youtube.com":["8.8.8.8","5.5.5.5"]}
my_dict2 = {"www.gmail.com":"9.9.9.1"}

חיבור בין מילונים שונים
my_dict.update(my_dict2)
print(my_dict)
'''
'''
my_dict = {"www.facebook.com": "8.8.8.8","www.youtube.com":["8.8.8.8","5.5.5.5"]}
##מדפיס אורך של המילון
print(len(my_dict))
'''
'''
my_dict = {"www.facebook.com": "8.8.8.8","www.youtube.com":["8.8.8.8","5.5.5.5"]}
להדפיס ערך של מילת מפתח מסויימת
print(f"IP adress is : {my_dict['www.facebook.com']}")
'''
'''
my_dict = {"www.facebook.com": "8.8.8.8","www.youtube.com":["8.8.8.8","5.5.5.5"]}
my_dict["www.facebook.com"] = 0
print(my_dict.keys())
print(my_dict.values())
'''
'''
my_dict = {"www.facebook.com": "8.8.8.8","www.youtube.com":["8.8.8.8","5.5.5.5"]}
print("www.youtube.com" in my_dict)
print("8.8.8.8" in my_dict.values())
'''
'''
מילון עם שמות של אנשים והכסף שלהם
balance_dict = {
    "dan": 5000,
    "david": 6000,
    "itzik": 7000
}
summary = balance_dict['dan'] + balance_dict['itzik']
print(f"the balance of the first and last combained is : {summary}")
balance_dict.update({"dudu":summary})
print(balance_dict)
print(len(balance_dict))
print("dan" in balance_dict)
'''