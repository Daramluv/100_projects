#Adding_even_numbers
import random
target = random.randint(2,100)

sum = 0

for i in range(2,target+1):
    if i % 2 == 0:
        sum += i
print(f"Random target number is {target}")
print(f"total even number in range 2 to {target} is {sum}")