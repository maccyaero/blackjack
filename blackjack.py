import random


card_values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_values =[]
comp_values =[]
random_num = random.choice(card_values)
user_values.append(random_num)
random_num = random.choice(card_values)
user_values.append(random_num)
random_num = random.choice(card_values)
comp_values.append(random_num)
random_num = random.choice(card_values)
comp_values.append(random_num)

print(f"your values are {user_values} and sum is {sum(user_values)}")
print(f"Comp values are {comp_values[0]} and sum is {sum(comp_values)}")
users_choice = input("Do you want to draw another card ? (y or n)")
while (users_choice == "y"):
    if (users_choice == "y"):
        random_num = random.choice(card_values)
        user_values.append(random_num)
        print(f"your values are {user_values} and sum is {sum(user_values)}")
        users_choice = input("Do you want to draw another card ? (y or n)")
while(sum(comp_values)<14):
    random_num = random.choice(card_values)
    comp_values.append(random_num)

if (sum(user_values) > sum(comp_values) and sum(user_values)<21):
    print("You Won")
elif(sum(user_values) == sum(comp_values)):
    print("draw")
else:
    print("You lost")

