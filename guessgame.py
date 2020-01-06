try:
    def mycode():
        print("you have 5 guess. Find the secret number between 1-10")
        a = 6
        b = 0
        count = 0
        gcount = 0
        max_error = 5
        while count < max_error:
            b = int(input("Your guess: "))
            count += 1
            gcount += 1
            print("Guess")
            print(gcount)
            if b < a:
                print("higher than that")
            elif b > a:
                print("lower than that")
            elif b == a:
                print("You won, thats the one")
                break
            else:
                print("you lose")
    mycode()

except ValueError:
    print("---------------------------")
    print("Please enter only numbers !")
    print("---------------------------")
    mycode()
