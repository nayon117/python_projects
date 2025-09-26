name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

ans = input("You are on a dirt road. choose which way you want to go left or right : ").lower()

if ans == "left":
    ans = input("you come to a river. you have two option type walk to walk around or type swim to swim across: ").lower()
    if ans == "walk":
        print("You walk around many miles and you ran out of water and you loose the game")
    elif ans == "swim":
        print("You swam across and were eated by and alligator")
    else: 
        print("Not a valid option. you loose!")

elif ans == "right":
    ans = input("You come to a bridge. it looks woobly want to cross it or head back.(cross/back) ? : ").lower()
    if ans == "cross":
       ans = input ("you try to cross the road and meet strangers . do you want to talk with them(yes/no) ? : ").lower()
       if ans == "yes" :
            print("you talk to the stranger and they give you gold and you win!")
       elif ans == "no":
           print("you ignore the stranger and they are offended and you loose")
       else :
        print("Not a valid option. you loose!")
           
    elif ans == "back":
        print("you go back and you loose the game")
    else :
        print("Not a valid option. you loose!")

else:
    print("Not a valid option. you loose!")

print("Thank you for trying",name)
