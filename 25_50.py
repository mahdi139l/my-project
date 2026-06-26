#26
# s=input("enter your number?").strip()
# valid=True
# if len(s) !=11:
#     valid=False
# elif not (s[0]=="0" and s[1]=="9" ):
#     valid=False 
# else:
#     for ch in s :
#      if ch < "0" or ch > "9" :
#         valid=False
#         break
# if valid :
#     print("valid")
# else:
#     print("unvalid")    




#27 help 
# def number(username):
#     if len(username)==0:
#      if username[0]=="0" or username[-1]=="0":
#         return"invalid"
#     for ch in username :
#         if not(ch.isalpha() or ch.isdigit()):
#             return"invalid"
#         return"valid"
#     print(validate(input("enter?")))
# print(validate(input("enter ?")))
# print(validate(input("enter?")))
# print(validate(input("enter?")))



#28
# email = input("enter?").strip()
# if email.count("@") == 1:
#     valid = True
#     for ch in email:
#         if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9' or ch == '@' or ch == '.'):
#             valid = False
#             break
#     if valid:
#         print("Valid")
#     else:
#         print("Invalid")
# else:
#     print("Invalid")



#29
# num=int(input("enter?"))
# if num % 2==0 
# n="number is even "
# else:
# n="number is even "
# print(n)

#29
# num=input("enter?")
# print("number is even" if num % 2 == 0 else "number is odd")


#30
# n=int(input("enter your number?"))
# #print(f"you have a {n} massage")
# print("you have no message" if n == 0 else f"you have a {n} massage")


#31
# name =input("enter your name?")
# if name =="ali" :
#     print(name.upper)


#31
# name = input("enter your name? ")
# if name.lower().startswith("ali"):
#     print(name.upper())
# else:
#     print(name.lower())



#32
# n = input("enter gavab 21*2: ").strip()

# c = ["42", "forty-two", "forty two", "FoRtY-tWo"]

# if n in c :
#     print("yes")
# else:
#     print("no")




#33
# n=input("what time is it ?")
# if 7 or 8 :
#     print("it is a breakfast time.")
# if n==12 or 13 :
#     print("it is a lunch time.")
# if n==21 or 22 :
#     print ("it is a dinner")        




#33
# time = input("what time is it? ").strip()
# hour, minute = map(int, time.split(":"))

# if 7 <= hour < 9:   
#     print("--> break fast time")
# elif 12 <= hour < 14:  
#     print("--> lunch time")
# elif 21 <= hour < 23:  
#     print("--> dinner time")
# else:
#     print("--> not meal time")




#34
# n=input("enter ?")
# if n.startswith("hello"):
#     print("hesab shoma 0 dollar ")
# elif n.startswith("h"):
#     print("hesab shoma 20 dollar ")
# elif n.startswith(""):
#     print("error")
# else:
#     print("hesab shoma 100 dollar ")    



#35
# n=input("enter your name?")
# if n.count("a")>1:
#     print("yes")
# else:
#     print("no")  
# 
# 


#37
# n = int(input("enter?"))
# i = 2
# c = []
# while i * i <= n:
#     if n % i == 0:
#         c.append(i)
#         while n % i == 0:
#             n /= i
#     i += 1
# if n > 1:
#     c.append(n)

# for p in c:
#     print(p)



#38
# n = int(input("enter?"))
# i = 2
# c = 1
# while i * i <= n:
#     while n % i == 0:
#         c = i
#         n /= i
#     i += 1
# if n > 1:
#     c = n
# print(c)








#39
# while True:
#     n = input("enter your number?")
#     try:
#         n = int(n) 
#         break                 
#     except ValueError:
#         print("error error enter yor number")
# print("your number:",n)









#40
# number=input("enter your number?")
# amaliat=input("enter your(+ - * /)")
# number2=input("enter your number?")




#40 help 
# def get_number(msg):
#     while True:
#         user_input = input(msg)
#         try:
#             return int(user_input)
#         except ValueError:
#             print("خطا! لطفاً یک عدد صحیح وارد کنید.")
# num1 = get_number("عدد اول را وارد کنید: ")
# while True:
#     op = input("عملیات را وارد کنید (+ - × ÷): ")
#     if op in ["+", "-", "×", "÷"]:
#         break
#     else:
#         print("عملیات نامعتبر! فقط + - × ÷ مجاز است.")
# while True:
#     num2 = get_number("عدد دوم را وارد کنید: ")
#     if op == "÷" and num2 == 0:
#         print("خطا! در تقسیم عدد دوم نباید صفر باشد.")
#     else:
#         break
# if op == "+":
#     result = num1 + num2
# elif op == "-":
#     result = num1 - num2
# elif op == "×":
#     result = num1 * num2
# elif op == "÷":
#     result = num1 / num2
# print("نتیجه:", result)

#41
# number = int(input("enter your number?"))
# for i in range(1, number + 1):
#     print(" ".join(["*"] * i))





#42
# number = int(input("enter your number?"))
# for i in range(1, number + 1):
#     print("   " * (number - i) + " ".join(["*"] * (2 * i - 1)))
# for i in range(number - 1, 0, -1):
#     print("   " * (number - i) + " ".join(["*"] * (2 * i - 1)))






#43 help 
# number=int(input("enter your number?"))
# for i in range(1,number+1):
#     for a in range(1,i+1) :
#         print(" ".join (str(a)))




#44
# number = int(input("enter ?"))
# for i in range(1, number + 1):
#     print(" ".join([str(i)] *   i))


#45
# number = int(input("enter?"))
# for i in range(1, number + 1):
#     print(" ".join([str(i)] * (number - i + 1)))




#46
# number = int(input("enter?"))
# for i in range(number):
#     print(" ".join([str(number)] * (number - i)))



#47
# number = int(input("enter"))
# for i in range(number, 0, -1):
#     n = [str(j) for j in range(0, i + 1)]
#     print(" ".join(n))



#48
# n = int(input("enter your number? "))
# for i in range(n, 0, -1):
#     for a in range(i):
#         print(i, end=" ")
#     print()




#49
# n = int(input("enter your number? "))
# for i in range(1, n + 1):
#     for a in range(i, 0, -1):
#         print(a, end=" ")
#     print()




#50
# n = int(input("enter your number? "))
# for i in range(n, 0, -1):
#     for a in range(i, 0, -1):
#         print(a, end=" ")
#     print()





#operator

# import csv
# irancell_users = []
# hamrah_users = []
# with open("users.csv", newline='', encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for satr in reader:
#         shomare = satr['phone_number']
#         esm = satr['name'].upper()  
#         if shomare.startswith(("093","099")):
#             satr['name'] = esm
#             satr['modir'] = "Irancell"
#             irancell_users.append(satr)
#         elif shomare.startswith(("091","092")):
#             satr['name'] = esm
#             satr['modir'] = "Hamrah"
#             hamrah_users.append(satr)
# with open("irancell_users.csv", "w", newline='', encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=irancell_users[0].keys())
#     writer.writeheader()
#     writer.writerows(irancell_users)
# with open("hamrah_users.csv", "w", newline='', encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=hamrah_users[0].keys())
#     writer.writeheader()
#     writer.writerows(hamrah_users)











