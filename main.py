num = int(input("enter a number"))

alafiem = num // 1000
meot = (num // 100) % 10
asharot = (num // 10) % 10
ahadot = num % 10

print(f"{alafiem},{meot},{asharot},{ahadot}")
