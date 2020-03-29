#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


random.seed(0)
WIN_SCORE = 100


# In[3]:


class Player():

    def __init__(self):
        self.score = 0
        self.turn_total = 0

    def increment_score(self, random_score):
        self.turn_total += random_score

    def hold(self):
        self.score += self.turn_total

    def lose(self):
        self.turn_total = 0

    def __str__(self):
        return '**************' + '\nTurn Total:' +             str(self.turn_total) + '\nScore:' + str(self.score) + '\n\n'


# In[4]:


class Game():

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.die = Die()
        self.chance = 1
        self.roll_value = 0
        print('Welcome to the game: ')

    def check_win(self):
        if (self.player1.score >= WIN_SCORE):
            print('Winner = P1')
            return 1

        elif (self.player2.score >= WIN_SCORE):
            print('Winner = P2')
            return 1
        return 0

    def check_lose_on_one(self):
        if self.roll_value == 1:
            if self.chance:
                self.player1.lose()
                self.chance = 0
            else:
                self.player2.lose()
                self.chance = 1
            return 1
        return 0

    def which_player_choice(self):
        if self.chance:
            print('Player 1 Choice')
        else:
            print('Player 2 Choice')

    def check_user_choice(self, user_choice):
        if user_choice == 'K':
            self.roll_value = self.die.roll()
            print('DIE ROLL: ', self.roll_value)
            if not self.check_lose_on_one():
                if self.chance:
                    self.player1.increment_score(self.roll_value)
                else:
                    self.player2.increment_score(self.roll_value)

        elif user_choice == 'C':
            if self.chance:
                self.player1.hold()
                self.player1.lose()
                self.chance = 0
            else:
                self.player2.hold()
                self.player2.lose()
                self.chance = 1

        else:
            print('Wrong input')

    def show_status(self):
        print('Player1')
        print(self.player1)
        print('Player2')
        print(self.player2)


# In[5]:


class Die():

    def roll(self):
        return random.randint(1, 6)


# In[ ]:


def main():
    game = Game()
    print('Welcome to the game: ')

    while True:
        if game.check_win():
            break
        game.which_player_choice()
        user_choice = str(input('Enter C for hold and K for roll: '))
        game.check_user_choice(user_choice)
        game.show_status()

if __name__ == '__main__':
    main()


# In[ ]:




