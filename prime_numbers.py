#prime_numbers

def prime_checker(number):
    if number <= 1:
        print("It's not a prime number.")
        return
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

end_of_game = False
while not end_of_game:
    n = int(input("Please provide an integer: "))
    prime_checker(n)
    try_again = input("Do you want to try again? Y/N: ").lower()
    if try_again == "y":
        prime_checker(n)
    else:
        end_of_game = False
        print("Goodbye!")
        exit()
