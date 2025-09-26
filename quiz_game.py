print("Welcome to my computer quiz")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! let's play :) ")

score = 0

answer = input("1. What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    score += 1
else:
    print("Wrong answer")
   

answer = input("2. What does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print("Correct!")
    score += 1
else:
    print("Wrong answer")


answer = input("3. What does RAM stand for? ")
if answer.lower() == "random access memory" :
    print("Correct!")
    score += 1
else:
    print("Wrong answer")


answer = input("4. What does PSU stand for? ")
if answer.lower() == "power supply unit" :
    print("Correct!")
    score += 1
else:
    print("Wrong answer")


answer = input("5. Who is the founder of Microsoft? ")
if answer.lower() == "bill gates" :
    print("Correct!")
    score += 1
else:
    print("Wrong answer")

print("You got correct " , score , "questions")
print("Your percentage is ", (score /5) * 100, "%" )
