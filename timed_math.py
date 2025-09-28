import random 
import time

OPERATORS = ["+","-","*"]
OPERAND_MIN = 3
OPERAND_MAX = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(OPERAND_MIN,OPERAND_MAX)
    right = random.randint(OPERAND_MIN,OPERAND_MAX)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start !")
print("--------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time
print("--------------------")
print("Nice work", "your accuracy is ", ((10 - wrong) / 10) * 100)
print("you finished in ",round(total_time,2), "seconds")
