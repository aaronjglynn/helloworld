def main():
    fruit_basket = ["apple","banana","pear","blueberry","melon"]
    guess = raw_input("What's your guess?\n")
    if str(guess) in fruit_basket:
        print("you're right!")
    else:
        print("sorry charlie")

main()
