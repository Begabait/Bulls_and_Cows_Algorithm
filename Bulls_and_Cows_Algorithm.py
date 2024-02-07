import random


class Human:
    def __init__(self):
        self.bulls = 0
        self.cows = 0


class Computer:
    def __init__(self):
        self.bulls = 0
        self.cows = 0
        self.number = ''.join([str(i) for i in random.sample([i for i in range(1, 10)], 4)])
        self.possible = [str(i) for i in range(1111, 10000) if not check_num(str(i))]
        self.guess = None

    def new_guess(self):
        self.guess = self.possible.pop(self.possible.index(random.choice(self.possible)))


def check_num(num):
    for i in num:
        if num.count(i) > 1 or i == '0':
            return True
    else:
        return False


human = Human()
computer = Computer()


def compare_num(num1, num2, score):

    res = 0
    for i in range(4):
        if num1[i] == num2[i]:
            res += 1
        elif num2[i] in num1:
            res += 0.5

    return score == res


while True:
    guess = input('\nYour guess:\n')

    human.bulls = 0
    for i in range(4):
        if guess[i] == computer.number[i]:
            human.bulls += 1

    human.cows = 0
    for i in range(4):
        if guess[i] != computer.number[i] and guess[i] in computer.number:
            human.cows += 1

    if human.bulls == 4:
        print('You win!')
        break
    else:
        print(f'Bulls: {human.bulls}\nCows: {human.cows}\n')

    computer.new_guess()
    print(f'My guess is: {computer.guess}')

    computer.bulls = int(input('How many bulls are there:\n'))

    if computer.bulls == 4:
        print('Ooo, I win, good game!')
        print(f'My number was: {computer.number}')
        break

    computer.cows = int(input('How many cows are there:\n'))

    if computer.bulls == 0 and computer.cows == 0:
        to_remove = []
        for i in computer.possible:
            for j in computer.guess:
                if j in i:
                    to_remove.append(i)
                    break

        for i in to_remove:
            computer.possible.pop(computer.possible.index(i))

    if computer.cows + computer.bulls == 4:
        to_remove = []
        for i in computer.possible:
            for j in computer.guess:
                if j not in i:
                    to_remove.append(i)
                    break

        for i in to_remove:
            computer.possible.pop(computer.possible.index(i))

    score = computer.bulls + computer.cows * 0.5
    to_remove = []
    for num2 in computer.possible:
        if not compare_num(computer.guess, num2, score):
            to_remove.append(num2)

    for i in to_remove:
        computer.possible.pop(computer.possible.index(i))
