
## מילון עם שמות וכמות כסף
balance_dict = {
    "dan": 5000,
    "david": 6000,
    "itzik": 7000
}
summary = balance_dict['dan'] + balance_dict['itzik']
print(f"the balance of the first and last combained is : {summary}")
balance_dict.update({"dudu":summary})
print(balance_dict)
print("dan" in balance_dict)
##אם לא קיים אז זה לא מעדכן אלה מוסיף
balance_dict["max"] = summary + 2000
print(balance_dict)
balance_dict["dan"] += 3000
print(len(balance_dict))
print(balance_dict)
