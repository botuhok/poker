import os
import time
from Deck import Deck
from Gamer import Gamer
from Hand import Hand

from termcolor import colored, cprint
from colorama import init
from colorama import Fore, Back, Style
init()

begin_scores = 1000


# define clear function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def head(gamer):
    clear()

    color = "yellow"
    print(colored("                   dP", color))
    print(colored("                   88", color))
    print(colored(" 88d888b. .d8888b. 88  .dP  .d8888b. 88d888b.", color))
    print(colored(" 88'  `88 88'  `88 88888\"   88ooood8 88'  `88", color))
    print(colored(" 88.  .88 88.  .88 88  `8b. 88.  ... 88", color))
    print(colored(" 88Y888P' `88888P' dP   `YP `88888P' dP", color))
    print(colored("~88~oooooooooooooooooooooooooooooooooooooooooo", color))
    print(colored(' dP', color))
    print()
    print('SCORES: ' + colored(gamer.scores, 'green'), end = '                          ')
    print('BET: ' + colored(str(gamer.bet), 'green'))
    print()

def menu(gamer):
    while gamer.scores > 0:
        deck1 = Deck()                          # создаём новую колоду
        deck1.shuffle()                         # перемешиваем
        hand = Hand(deck1)                      # берём из колоды список из 5 карт
        head(gamer)
        print('Your bet (100):', end = ' ')
        bet = input()
        if bet == 'q' or bet == 'Q':
            quit()
        try:
            bet = int(bet)
            if bet > gamer.scores:
                raise ValueError('bet must be < scores')
        except:
            print()
            print(colored('Set default bet to 100', 'red'))     # ставка по умолчанию
            bet = 100
            time.sleep(2)
        gamer.bet = bet
        head(gamer)
        hand.show()
        print("Would you like to " + Fore.GREEN + "change" + Style.RESET_ALL + " some cards or " + Fore.RED + "finish?")
        print(Style.RESET_ALL)
        print("Press " + Fore.GREEN + '1' + Style.RESET_ALL + ' for ' + Fore.GREEN + 'change' + Style.RESET_ALL)
        print(Style.RESET_ALL)
        print("Press " + Fore.RED + '2' + Style.RESET_ALL + ' for ' + Fore.RED + 'finish' + Style.RESET_ALL)
        choice = input()
        if choice == '1':
            head(gamer)
            hand.show()
            print("   1        2        3         4        5 ")
            print('          Select card\'s numbers:')
            try:
                choise_lst = list(i for i in map(int, input().split()) if i <= 5)
            except:
                choise_lst = []

            hand.change(choise_lst)
            result = hand.check()
            gamer.check(result)
            head(gamer)
            hand.show()
            print(Fore.GREEN + 'You have ' + Fore.RED + result + Style.RESET_ALL)
        else:
            head(gamer)
            hand.show()
            print(Fore.GREEN + "You choose finish. Ok, let's see what you have...")
            print(Style.RESET_ALL)
            result = hand.check()
            print(Fore.GREEN + 'You have ' + Fore.RED + result + Style.RESET_ALL)
            gamer.check(result)
            print(gamer)
        time.sleep(3)
    print(colored('Game over!', 'red'))

print('todo: check change list! (try,except)')
gamer1 = Gamer(begin_scores)
menu(gamer1)

