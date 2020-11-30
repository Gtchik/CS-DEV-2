# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:42:17 2020

@author: gtchi
"""
from random import randint
from Word import *

class Game:  
    def __init__(self):
        self.__words=[]
        self.__playedWords=[]
        self.__score=[]
    
    def setWordsFromFile(self, url): #self
        with open(url) as f:
            wordsList = f.read().splitlines()
        self.__words = [ Word().setWord(wordsList[i]) for i in range(len(wordsList))]
        return self
    def __removeWords(self,val): #self
        self.__words.remove(val)
        return self
    def getWords(self): #array
        return self.__words

    def __addPlayedWords(self, word): #self
        self.__playedWords.append(word)
        return self
    def getPlayedWord(self): #array
        return self.__playedWords

    def __addScore(self, score): #self
        self.__score.append(int(score))
        return self
    def getScore(self): #array
        return self.__score
    
    def getMaxScore(self): #integer
        return min(self.__score)
    
    def start(self):
        word = self.getWords()[randint(0,len(self.getWords())-1)]
        while 1:
            print(f"Plus que {8-word.getTour()} tour(s)")
            print(word.getCurrent())
            letter = input(' Entrez votre lettre : ')
            retour =  word.checkLetter(letter)
            if not retour[0]:
                print(retour[1])
                if not retour[2]:
                    break
            print('\n\n')
            
        self.__addScore(word.getTour())
        self.__removeWords(word).__addPlayedWords(word)
        print(f"Au mieux vous avez devinés en {self.getMaxScore()} tours ! Bravo !")
        if input('Voulez vous rejouer ? (y/n): ')=='y':
            self.start()
        return self