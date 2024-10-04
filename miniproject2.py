import random
import time

operators = ["-","+","*"]
min_operand = 3
max_operand = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_operand,max_operand)
    operator = random.choice(operators)
    right = random.randint(min_operand,max_operand)

    exp = str(left) + operator + str(right)
    answer = eval(exp)
    return exp,answer
wrong = 0
input("press enter to start!")
print("---------------------")
start_time = time.time()
for i in range(total_problems):
    exp,answer = generate_problem()
    while True:
        guess = input("problem #"+str(i+1)+":"+exp+"=")
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()
total_time = end_time - start_time
print("good job! you finished in ",total_time," s")
print("you made ",wrong," wrong !")
print("---------------------")