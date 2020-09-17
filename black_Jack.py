import random


class Card:
    def __init__(self, score):
        self.score = score

    def getScore(self):
        return self.score


class Chervy(Card):
    def __init__(self, score):
        Card.__init__(self, score)

    def getMast(self):
        return "черви"


class Buby(Card):
    def __init__(self, score):
        Card.__init__(self, score)

    def getMast(self):
        return "буби"


class Pika(Card):
    def __init__(self, score):
        Card.__init__(self, score)

    def getMast(self):
        return "пика"


class Kresty(Card):
    def __init__(self, score):
        Card.__init__(self, score)

    def getMast(self):
        return "крести"


def comp_gamer(a, b):
    summ = 0
    while summ <= 15:
        choice = cards.pop(random.randint(a, b))
        b -= 1
        summ += choice.getScore()
    return summ


# making card deck
cards = []
for i in range(2, 12):
    if i != 5:
        cards.append(Chervy(i))
        cards.append(Buby(i))
        cards.append(Pika(i))
        cards.append(Kresty(i))

name_cards = {6: "шестёрка", 7: "семёрка", 8: "восьмёрка", 9: "девятка", 10: "десятка", 2: "валет", 3: "дама",
              4: "король", 11: "туз"}
summ = 0
a, b = 0, 35
while True:
    go = input("Would you like to get a card?: Y - yes, N - no ")
    if go == 'Y' or go == 'y':
        choice = cards.pop(random.randint(a, b))
        b -= 1
        print("Your choice:", name_cards[choice.getScore()], choice.getMast())
        summ += choice.getScore()
        if summ > 21:
            print('_' * 40)
            print("You have got score:", summ)
            break
        else:
            print("You have score:", summ)
    else:
        print('_' * 40)
        print("You have got score:", summ)
        break

comp_score = comp_gamer(a, b)
print('_' * 40)
print("Computer gamer have got score", comp_score)
print('_' * 40)
if comp_score > 21 >= summ:
    print("You are a WINNER")
elif comp_score > 21 and summ > 21:
    print("You and computer gamer are LOOSERS")
elif comp_score == summ and summ < 22:
    print("You results are equal")
else:
    print("You are a WINNER" if comp_score < summ < 22 else "You are a lOOSER")