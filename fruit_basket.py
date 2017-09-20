def guess_fruit(basket):
    guess = raw_input("What's your guess?\n")
    return (guess in basket)

def main():
    fruit_basket = ["apple","banana","pear","blueberry","melon"]
    guess_num = 0
    while guess_num < 5:
        result = guess_fruit(fruit_basket)
        if result:
            print("Nice going!")
            return
        elif not result:
            print("Incorrect")
            guess_num += 1
        else:
            print("You're all outta time punk.")
            return
main()
