print("MENU\n1.insert a number and ** by 3\n"
      "2.insert 4 IPs to a list and print it\n"
      "3.insert 4 entries to DNS_dictionary and print it\n"
      "4.check if a string is polindrom")

user_input = input("enter a number ! : ")
if user_input == "1":
    print(int(input("enter a number : "))**3)
elif user_input == "2":
    ip_list = []
    ip_list = input("insert 4 IPs : ").split(",")
    print(f"IP List : {ip_list}")
elif user_input == "3":
    DNS_Dictonary = {}
    for i in range(2):
       DNS_Dictonary.update({input("enter an entrie "):(input("enter an ip"))})
    print(DNS_Dictonary)
elif user_input == "4":
     string = input("enter a string :")
     if string == string[::-1]:
         print("it is polindrom ! ")
     else:
         print("not polindrom")





