#!/usr/bin/env python3
import ntplib
import itertools
import ast 
import random

c = ntplib.NTPClient()
response = c.request('time.cloudflare.com', version=3)

values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts','Clubs','Diamonds','Spades']

deck_of_cards = list(itertools.product(values, suites))

def initialise():
    timestamp_miliseconds = int(response.recv_time*1000)
    shuffled_deck_of_cards = deck_of_cards.copy()
    random.Random(timestamp_miliseconds).shuffle(shuffled_deck_of_cards)

    return shuffled_deck_of_cards

def greet():
    print(r"""
.------..------..------..------.     .------..------..------..------.     .------..------..------..------..------.
|P.--. ||R.--. ||O.--. ||F.--. |.-.  |D.--. ||I.--. ||N.--. ||G.--. |.-.  |P.--. ||O.--. ||K.--. ||E.--. ||R.--. |
| :/\: || :(): || :/\: || :(): ((5)) | :/\: || (\/) || :(): || :/\: ((5)) | :/\: || :/\: || :/\: || (\/) || :(): |
| (__) || ()() || :\/: || ()() |'-.-.| (__) || :\/: || ()() || :\/: |'-.-.| (__) || :\/: || :\/: || :\/: || ()() |
| '--'P|| '--'R|| '--'O|| '--'F| ((1)) '--'D|| '--'I|| '--'N|| '--'G| ((1)) '--'P|| '--'O|| '--'K|| '--'E|| '--'R|
`------'`------'`------'`------'  '-'`------'`------'`------'`------'  '-'`------'`------'`------'`------'`------'
""")
    print("Welcome to Prof Ding's Poker Game!")
    print("I'm going to shuffle the deck of cards and give you the first 5 cards")
    print("With that, you have to guess the entire sequence of the cards")
    print("If you get it right, you win")
    print("If you get it wrong, you lose")
    print("Good luck!\n")

def collect_input(shuffled_deck_of_cards):
    print("The first card is " + str(shuffled_deck_of_cards[0]))
    print("The second card is " + str(shuffled_deck_of_cards[1]))
    print("The third card is " + str(shuffled_deck_of_cards[2]))
    print("The fourth card is " + str(shuffled_deck_of_cards[3]))
    print("The fifth card is " + str(shuffled_deck_of_cards[4]) + "\n")

    input_shuffled_deck_of_cards = input("Can you list the entire sequence of the cards including the first five?\n")

    try:
        input_shuffled_deck_of_cards = ast.literal_eval(input_shuffled_deck_of_cards)
    except:
        print("\nYou lose, Prof Ding is very disappointed in you. Seems like you need to take his module. Try again!\n")
        print("The correct answer is \n\n" + str(shuffled_deck_of_cards))
        exit()

    if input_shuffled_deck_of_cards == shuffled_deck_of_cards:
        f = open("/home/user/flag.txt", "r")
        print("\nYou win! Prof Ding is very proud of you!\n")
        print("The flag is " + f.read())
    else:
        print("\nYou lose, Prof Ding is very disappointed in you. Seems like you need to take his module. Try again!\n")
        print("The correct answer is \n\n" + str(shuffled_deck_of_cards))

if __name__ == "__main__":
    shuffled_deck_of_cards = initialise()
    greet()
    collect_input(shuffled_deck_of_cards)