dividend = int(input("Please Enter the number you want >> "))

for divisor in range(2,11):
    if not (dividend % divisor):
        print(f"{divisor} is divisible by {dividend} without a remainder ")