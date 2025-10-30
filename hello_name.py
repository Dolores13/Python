name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python :)")

age = input("How old are you? ")
print(f"You are {age} years old!")  

print(f"In 5 years, you will be {int(age) + 5} years old.") 

answer = input("Do you like to know your age in 10 years? (yes/no)")
if answer.lower() == 'yes':
    print(f"In 10 years, you will be {int(age) + 10} years old.")
else:
    print("Alright, have a great day!")