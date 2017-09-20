def main():
    fruit_basket = ["apple","banana","pear","blueberry","melon"]
    guess = raw_input("What's your guess?\n")
    while str(guess) not in fruit_basket:
        print("you're not correct!")
        guess = raw_input("What's your next guess?\n")
    else:
        print("great job charlie!")

main()
