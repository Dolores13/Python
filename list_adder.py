numbers = [] 

for i in range(5):
    num = int(input(f"Enter a number to add to the list: {i+1} "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print(f"\nThe numbers are: {numbers}")
print(f"The total sum is: {total}")
print(f"The average is: {average}")
