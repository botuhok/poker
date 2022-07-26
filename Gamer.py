class Gamer:
    def __init__(self, scores):
        self.scores = scores
        self.bet = 100

    def __repr__(self):
        return f'SCORES: {self.scores}'

    def check(self, hand_check):
        self.hand_check = hand_check
        if hand_check == "Nothing":
            self.scores -= self.bet
        elif hand_check == 'pair':
            self.scores += self.bet*2
        elif hand_check == 'two pairs':
            self.scores += self.bet*3
        elif hand_check == 'trips':
            self.scores += self.bet*4
        elif hand_check ==  'straight':
            self.scores += self.bet*6
        elif hand_check == 'flush':
            self.scores += self.bet*8
        elif hand_check == 'full house':
            self.scores += self.bet*12
        elif hand_check == 'four of kind':
            self.scores += self.bet*25
        elif hand_check == "straight flush":
            self.scores += self.bet*50
        elif hand_check == "royal flush":
            self.scores += self.bet*100


    def win(self, num):
        #d = {'full house', }
        self.scores += num

