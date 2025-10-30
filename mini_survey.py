survey = {}
for i in range (1,3):
    print(f"\n--- Person {i} ---")
    name = input("Enter name: ")
    age = int(input(f"Enter age: "))
    contry = input("Enter country: ")
    survey[name] = {'age': age, 'country': contry}
print("\nSurvey Results:")
j = 1
for name, info in survey.items():
    print(f"person {j}: {name} is {info['age']}, years old and lives in {info['country']}") 
    j += 1

