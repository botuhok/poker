from random import shuffle
class Deck:
    def __init__(self):
        suits = ['♥', '♦', '♣', '♠']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(f'{value} {suit}')

    def __repr__(self):
        return 'Deck of ' + str(self.count()) + ' cards'

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)
    
    def _deal(self, num = 1):
        count = self.count()
        actual = min([num,count])            # чтобы предотвратить момент, когда нужно раздать больше, чем есть
        if count == 0:                       # если в колоде нет карт
            raise ValueError("All cards have been dealt!")
        ret = self.cards[-actual:]           # сохраняем нужное количество карт в отдельный список
        self.cards = self.cards[:-actual]    # убираем из списка розданные карты
        return ret
        
    def shuffle(self):                  # перемешивает колоду
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled!")
        shuffle(self.cards)
        shuffle(self.cards)

    def deal_card(self):                # вытаскивает 1 карту из колоды
        return self._deal(1)[0]

    def deal_hand(self, n):             # вытаскивает n карт из колоды
        self.n = n
        return self._deal(n)
