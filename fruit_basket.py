def main():
    fruit_basket = ["apple","banana","pear","blueberry","melon"]
    guess = raw_input("What's your guess?\n")
    guess_num = 1 
    while guess_num <= 5:
        if guess in fruit_basket:
            print("Nice going!")
            return
        elif guess not in fruit_basket and guess_num < 5:
            print("Incorrect")
            guess = raw_input("What's your guess?\n")
            guess_num += 1
        else:
            print("You're all outta time punk.")
            return
main()
