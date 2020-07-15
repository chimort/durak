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
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return f'{self.rank} {self.suit}'

class Deck:
    def __init__(self):
        suits = ['chervi', 'kresti', 'bubni', 'piks']

        ranks = [6, 7, 8, 9, 10, 11, 12, 13, 14]
        trumpSuit = random.choice(suits)#берем рандомную масть из всех остальных

        self.cards = []

        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)#делаем колоду карт
        random.shuffle(self.cards) #перемешиваем колоду

        self.trump = random.choice(self.cards)

    def check(self):#делаем проверку на козыря и делаем его сильнее обычных карт
        return [str(i) for i in self.cards]


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

def distribution(): #делаем раздачу
    on_hand = []

    for i in range(6):
        dist = d.cards[0]
        d.cards = d.cards[1:]

        on_hand.append(str(dist))
    print(f'у вас на руках {len(on_hand)} карт: {", ".join(on_hand)}')



def Gameplay():
    userChoise = input('введите 1 чтобы посмотреть козырь, введите 2 чтобы посмотреть ваши карты ')
    if userChoise == '1':
        return print(str(d.trump))
    elif userChoise == '2':
        return distribution()
    else:
        print('вы ввели что-то не то, попробуйте еще раз')
        return Gameplay()

if __name__ == "__main__":
    Gameplay()


input()
#start()
print(", ".join(d.check()))
