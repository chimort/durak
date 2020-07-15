'''
сделать колоду карт+
сделать козырь+
сделать раздачу+
сделать чтобы казырные карты были сильнее обычных
сделать геимплей
сделать конец
добавить что-то
'''

import random

class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        self.trump = []
        suits = ['chervi', 'kresti', 'bubni', 'piks']
        ranks = [6, 7, 8, 9, 10, 11, 12, 13, 14]
        trumpSuit = random.choice(suits)#берем рандомную масть из всех остальных
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))#делаем колоду карт
                self.cards = dict()
        random.shuffle(self.cards) #перемешиваем колоду

    def check(self):#делаем проверку на козыря и делаем его сильнее обычных карт
        return str(self.cards)


def start():
    userStart = input("Добро пожаловать в игру дурак, если вы хотите прочитать правила, то их нет, \n для того чтобы начать игру нажмите 1, \n для выхода нажмите 2 ")
    if userStart == '1':
        return Gameplay()
    elif userStart == '2':
        exit()
    else:
        print('у вас всего 2 варианта не пытайся писать что-то еще')
        return start()



d = Deck()

def Trump(): #делаем козырную карту
    trumpCard = random.choice(d.cards)
    print(f'козырь: {trumpCard}')


def distribution(): #делаем раздачу
    on_hand_cards = 0
    on_hand = []
    dist = random.choice(d.cards)
    while on_hand_cards < 6:
        if dist not in on_hand:
            on_hand.append(str(dist))
            on_hand_cards += 1
            dist = random.choice(d.cards)
    print(f'у вас на руках: {on_hand}')



def Gameplay():
    userChoise = input('введите 1 чтобы посмотреть козырь, введите 2 чтобы посмотреть ваши карты ')
    if userChoise == '1':
        return Trump()
    elif userChoise == '2':
        return distribution()
    else:
        print('вы ввели что-то не то, попробуйте еще раз')
        return Gameplay()



#start()
print(d.check())


