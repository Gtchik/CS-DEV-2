# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:28:52 2020

@author: gtchi
"""

class ConsoleUI():
    def __init__(self,game):
        self.__game = game
    def getGame(self):
        return self.__game
    
    def start(self):
        """Console game"""
        game = self.getGame()
        game.start()
        while True:
            print(f"Plus que {game.nbTour-game.getTour()} tour(s)")
            print(game.getCurrent().getHiddenWord())
            letter = input(' Entrez votre lettre : ')
            print(game.checkLetter(letter))
            print('\n\n')
            if game.getCurrent().getHiddenWord()==game.getCurrent().getWord():
                print('victoire!')
                break
            if game.getTour()==game.nbTour:
                print('Perdu...')
                print(f"Le mot etait {game.getCurrent().getWord()}")
                break
        game.end()
        print(f"Au mieux vous avez devinés en {game.getMaxScore()} tours ! Bravo !")
        if input('Voulez vous rejouer ? (y/n): ')=='y':
            self.consoleStart()