import random as r

class Player:
    def __init__(self, name):
        self.name = name
        self.pos = 0

    def __repr__(self):
        return self.name

class SnakesLadders:
    def __init__(self):
        self.players = []
        self.finish = 100
        players_no_prompt = int(input('Welcome to Snakes and Ladders! How many players would you like to start a new game with?\n...'))
        self.players_no = players_no_prompt
        cnt = 0
        while cnt < self.players_no:
            cnt += 1
            new_player = input('\nPlayer {} name: '.format(cnt))
            self.players.append(Player(new_player))
        self.pos_list = [player.pos for player in self.players]
        # print(self.pos_list)
        # print(self.players)
        print('\nGreat! Let\'s start a new game with {} players.'.format(self.players_no))


    def dice_roller(self):
        return r.randint(1,6)

    def play(self):
        k = 1
        while k:
            for player in self.players:
                if player.pos >= 100:
                    k = 0
                    print('{} wins!'.format(player.name))
            for player in self.players:
                play_prompt = input('\nIt\'s {}\'s turn! Hit enter to roll!'.format(player.name))
                die1 = self.dice_roller()
                die2 = self.dice_roller()
                distance = 0
                distance += die1
                distance += die2
                while die1 == die2:
                    play_again_prompt = input('You rolled two {}s!! Hit enter to roll again!'.format(die1))
                    die1 = self.dice_roller()
                    die2 = self.dice_roller()
                    distance += die1
                    distance += die2
                player.pos += distance
                if player.pos == 2:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 38
                if player.pos == 7:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 14
                if player.pos == 8:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 31
                if player.pos == 15:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 26
                if player.pos == 16:
                    print('Oh no! {} hit a snake!'.format(player.name))
                    player.pos = 6
                if player.pos == 21:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 42
                if player.pos == 28:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 84
                if player.pos == 36:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 44
                if player.pos == 46:
                    print('Oh no! {} hit a snake!'.format(player.name))
                    player.pos = 25
                if player.pos == 49:
                    print('Oh no! {} hit a snake!'.format(player.name))
                    player.pos = 11
                if player.pos == 51:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 67
                if player.pos == 62:
                    print('Oh no! {} hit a snake!'.format(player.name))
                    player.pos = 19
                if player.pos == 64:
                    print('Oh no! {} hit a snake!'.format(player.name))
                    player.pos = 60
                if player.pos == 71:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 91
                if player.pos == 74:
                    print('Oh no! {} hit a snake!'.format(player.name))
                    player.pos = 53
                if player.pos == 78:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 98
                if player.pos == 87:
                    print('Nice! {} hit a ladder!'.format(player.name))
                    player.pos = 94
                if player.pos == 89:
                    print('Oh no! {} hit a snake!'.format(player.name))
                    player.pos = 68
                if player.pos == 92:
                    print('Oh no! {} hit a snake!'.format(player.name))
                    player.pos = 88
                if player.pos == 95:
                    print('Oh no! {} hit a snake!'.format(player.name))
                    player.pos = 75
                if player.pos == 99:
                    print('Oh no! {} hit a snake!'.format(player.name))
                    player.pos = 80
                if player.pos >= 100:
                    print('{} wins!'.format(player.name))
                    k = 0
                    break
                print('{} is at position {}'.format(player.name, player.pos))
        return

game = SnakesLadders()
game.play()
