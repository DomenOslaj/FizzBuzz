print "Hallo and welcome to the FizzBuzz game."

while True:

    end = raw_input("Please select one number between 1 and 100: ")

    try:
        end = int(end)

        for num in range(1, end+1):         # loop counts from 1 to end+1 - whatever value does user select +1.
            if end+1 > 102:
                print "The biggest number you can enter is 100."
                break

            elif num % 3 == 0 and num % 5 == 0:
                print "FizzBuzz"

            elif num % 3 == 0:
                print "Fizz"

            elif num % 5 == 0:
                print "Buzz"

            else:
                print num

    except ValueError:   # if string or decimal
        print "Please select whole numbers only (No words and decimals)"

    ask = raw_input("Would you like to play one more time (y/n)? ")

    if ask.lower() == "n":
        print "Thank you for playing our game!."
        break

    elif ask.lower() != "n" and ask.lower() != "y":
        print "I understand Y and N only!"

    else:
        continue
