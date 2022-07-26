from termcolor import colored, cprint
class Hand:
    def __init__(self, deck):
        self.deck = deck
        self.hand = self.deck.deal_hand(5)
    
    def show(self):             # выводит то, что в руке
        #d = {'A ♥' : '🂱', '2 ♥' : '🂲', '3 ♥' : '🂳', '4 ♥' : '🂴', '5 ♥' : '🂵', '6 ♥' : '🂶', '7 ♥' : '🂷', '8 ♥' : '🂸', '9 ♥' : '🂹', '10 ♥' : '🂺', 'J ♥' : '🂻', 'Q ♥' : '🂽', 'K ♥' : '🂾',
        #     'A ♦' : '🃁', '2 ♦' : '🃂', '3 ♦' : '🃃', '4 ♦' : '🃄', '5 ♦' : '🃅', '6 ♦' : '🃆', '7 ♦' : '🃇', '8 ♦' : '🃈', '9 ♦' : '🃉', '10 ♦' : '🃊', 'J ♦' : '🃋', 'Q ♦' : '🃍', 'K ♦' : '🃎',
        #     'A ♧' : '🃑', '2 ♧' : '🃒', '3 ♧' : '🃓', '4 ♧' : '🃔', '5 ♧' : '🃕', '6 ♧' : '🃖', '7 ♧' : '🃗', '8 ♧' : '🃘', '9 ♧' : '🃙', '10 ♧' : '🃚', 'J ♧' : '🃛', 'Q ♧' : '🃝', 'K ♧' : '🃞',
        #     'A ♤' : '🂡', '2 ♤' : '🂢', '3 ♤' : '🂣', '4 ♤' : '🂤', '5 ♤' : '🂥', '6 ♤' : '🂦', '7 ♤' : '🂧', '8 ♤' : '🂨', '9 ♤' : '🂩', '10 ♤' : '🂪', 'J ♤' : '🂫', 'Q ♤' : '🂭', 'K ♤' : '🂮'}
        for i in self.hand:
            if i[-1] == '♥' or i[-1] == '♦':
                print(colored(f'[ {i} ]', 'red'), end = '  ')
            else:
                print(f'[ {i} ]', end='  ')
        print()
        print()
        
    def change(self, choise_lst):           # заменяет выбранные карты на карты из колоды(self.deck)
        choise_lst.sort(reverse=True)
        for i in choise_lst:
            self.hand.pop(i-1)
            self.hand.insert(i-1, *self.deck._deal())

    def _royal(self):                       # check royal flush
        values = []
        suits = set()
        for i in self.hand:
            values.append(i[0])
            suits.add(i[-1])
        values.sort()
        if values == ['1', 'A', 'J', 'K', 'Q'] and len(suits) == 1:
            return True

    def _straight(self):                    # check straight flush
        values = []
        suits = set()
        for i in self.hand:
            suits.add(i[-1])
            if i[0] == "J":
                values.append(11)
            elif i[0] == 'Q':
                values.append(12)
            elif i[0] =='K':
                values.append(13)
            elif i[0] == 'A':
                values.append(14)
            elif i[0] == '1':
                values.append(10)
            else:
                values.append(int(i[0]))
        values.sort()
        for i in range(len(values)-1):
            if values[i] != values[i+1] - 1:
                return False
        if len(suits) == 1:
            return "straight flush"
        else:
            return "straight"

    def _flush(self):
        suits = set()
        for i in self.hand:
            suits.add(i[-1])
        if len(suits) == 1:
            return True

    def _pairs(self):
        nums = [i[0] for i in self.hand]
        pairs = {nums[i] : nums.count(nums[i]) for i in range(len(nums))}
        if len(pairs) == 2:
            for key, value in pairs.items():
                if value == 3:
                    return f'full house'
                elif value == 4:
                    return f'four of kind'
        p = 0
        keys = []
        for key, value in pairs.items():
            if value == 2:
                p += 1
                keys += key
            elif value == 3:
                return f'trips'
        if p == 1:
            return f'pair'
        elif p == 2:
            return f'two pairs'
        return "Nothing"

        
    def check(self):                    # проверяет комбинации в руке
        if self._royal():
            return "royal flush"
        elif self._straight() == "straight flush":
            return "straight flush"
        elif self._pairs() == 'four of kind':
            return 'four of kind'
        elif self._pairs() == 'full house':
            return 'full house'
        elif self._flush():
            return 'flush'
        elif self._straight() == "straight":
            return "straight"
        return self._pairs()

