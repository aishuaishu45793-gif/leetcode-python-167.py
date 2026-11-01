number = int(input("Enter a number: "))
total = 0

for i in range(1, number):
    if number > 0 and number % i == 0:
        total += i

if number > 0 and total == number:
    print("Perfect number")
else:
    print("Not a perfect number")