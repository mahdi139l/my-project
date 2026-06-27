number = int(input("enter your number ? "))#.strip()
alamat = input("enter your a alamat (+ - * / )")#.strip()
number1 = int(input("enter your number ? "))#.strip()
# while True :
#     try :
#         n = int(input(" enter a alamat ?"))
#         break 
#     except ValueError :
#         print("is not alamat please enter a alamat .")
# if alamat == "*" , "+" , "-" , "/" :
#     print()



match alamat :
    case "+" :
     print("result:", number + number1 )
    case "-" :
     print("result:", number - number1 )
    case "*" :
     print("result:", number * number1 )
    case "/" :
     print("result:", number / number1 )
                            
                        
