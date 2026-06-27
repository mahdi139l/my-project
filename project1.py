#1
# a = input("enter? ")
# b = input("enter? ")
# c = input("enter? ")
# print(f"{a}-{b}-{c}")
# print(a + "-" + b + "-" + c)
# print(a, b, c, sep="-")
# print("{}-{}-{}".format(a, b, c))



#2
# numbers=input("enter number?(+ - )")
# numbers1=input("enter number?(+ - )")
# print(f"numbers are {numbers} and {numbers1} ")




#3
# name=input("enter your name?")
# family_name=input("enter your family name?")
# print(f"hello, {name}{family_name} . welcom to the program")




#4 help 
# float_number=input("enter your float number?")
# print("{:.1f}".format(float_number))



#5
# fruit=input("enter your fruit?")
# tedad=int(input("enter your teded fruit?"))
# print("i ate "+(" " + fruit ) * tedad +" yesterday")



#6
# number=int(input("enter your number?"))
# number1=int(input("enter your number?"))

# yekan_number=number%10
# yekan_number1=number1%10

# print( yekan_number + yekan_number1)




#7
# number=input("enter your number(three digit)?")
# digit1=int(number[0])
# digit2=int(number[1])
# digit3=int(number[2])
# print(digit1+digit2+digit3,"is sum"
# print(digit1*digit2*digit3,"is mutiply"))



#8
# nums = []
# while True:
#     try:
#         nums.append(int(input("enter?")))
#     except:
#         break
# for n in nums:
#     print(f"{n:03d}")


#9
# all_money= int(input("enter your all money?"))
# meghdarkharjshode=int(input("enter your meghdar kharj shode?"))
# remaining=all_money - meghdarkharjshode
# precent=(remaining / all_money)*100
# if precent.is_integer():
#  print(f"{int(precent)}%")
# else:
#  print(f"{percent:.2f}%")


#10
# tedad=input("enter?")
# print(f" i have {tedad.center(5)} apple ")


#11
# number=int(input("enter your number?"))
# print(f"{number : ,}")



#12
# name=input("enter your name?")
# print(name.upper())


#13
# n=input("enter?")
# print(n.rstrip())
# print()
# print(n.lstrip())




#14
# n=input("enter?")
# print(n.strip())




#15
# txt="refgghgfgfapplesddsgfd"
# if "apple" in txt :
#     print("yes there is  .")
# else:
#     ("no there isnt  ")   



#16 help 
# number=input("enter your number?")
# number=str(int(number))
# print(number)



#17
# num=input("enter your number?")
# num=str(int(num))
# print(len(num))
# print(num)



#18
# num=input("enter your number?")
# all_zero=num.count("0")
# num_no_leading_zeros =num.lstrip("0")
# num_strip=num.rstrip("0")
# meaning_fullzero=num_strip.count("0")
# print("meaning full zero :", meaning_fullzero)
# print("all zero:", all_zero)


#19 help
# name=str(input("enter your name?")).strip 
# print(name.lower())
# print(f"{name.center:*}")
#AttributeError: 'builtin_function_or_method' object has no attribute 'lower'


#20 
# n=input("enter ?")
# s=n.replace(':)', '😄').replace(':(', '☹️') 
# print('--> ' + s)  




#21
# number=input("enter your number?")
# count=0
# for digit in number:
#     if digit !="0":
#         count+=1
#         print(count)



#22
# fruit=input("enter your fruit name?")
# num=int(input("enter your number?"))
# print(f"i like {fruit.center(num)}")



#23
# n=input("enter>(deleto khali kon vali ba horof kochak va bozorg)")
# print(n.upper())
# print(n.lower())



#24 help 
# s=input("enter ?").strip ()
# word=s.split()
# out1 = " ".join(w.capitalize() for w in words)
# if len(word)>=1:
#     first=word[0].capitalize()
#     rest=" ".join(w.lower()for w in word[1:])
#     out2=first+" " rest if rest else"".strip()
# else:
#     out2="" 
#     out3=s.upper().replace(" " , "*")
# print("my name is", out1)
# print("my name is", out2)
# print("my name is", out3)




#25
# n=input("enter?(*)")
# n=str(int(n"*"))
# print(n)




#26
