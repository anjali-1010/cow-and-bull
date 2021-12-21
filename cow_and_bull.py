import random
def sec_list():
    list1=[0,1,2,3,4,5,6,7,8,9]
    list2=random.sample(list1,k=5)
    print(list2)
sec_list()
#     return list2
# def check_guess():
#     bull=[]
#     cow=[]
#     num=sec_list()
#     i=0
#     while i<=10:
#         number=int(input("enter a your gussing number"))
#         possition=int(input("enter a youur gussing possition"))
#         if number in num:
#             index = num.index(number)
#             if index==possition:
#                 if number not in bull:
#                     bull.insert(index,number)
#                     print("**bull** tha number and possition both are right..great""\n",bull)
#                 else:
#                    print("you Alrady used this digit")
#             else:
#                 cow.append(number)
#                 print("cow,this number is in list but possition is wrong please try agin...""\n",cow)
#         elif number not in num:
#             print("you guess is wrong")
#         if bull==num:
#             print("congratulations you win the game")
#             break
#         i=i+1
#         print(i,"Turn are left")
#     else:
#         print("you used all chances")
#     return bull
# def play_again():
#     while True:
#         again=int(input("if you want to play again press yas1 no2:"))
#         if again==1:
#             check_guess()
#         else:
#             print("thanks for enter in game...Have a nice day")
#             break
# play_again()
