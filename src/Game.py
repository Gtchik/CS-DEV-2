# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:42:17 2020
@Tp-2
@author: gtchi
"""
from random import choice
from Word import Word

class Game:
    nbTour=7
    def __init__(self, url: str):
        self.__playedWords=[]
        self.__score=[]
        self.__tour=0
        self.__current=''
        with open(url) as f:
            wordsList = f.read().splitlines()
            f.close()
        self.__words = [ Word(word) for word in wordsList]

    def __removeWords(self,val: str): #self
        self.__words.remove(val)
        return self
    def getWords(self): #array
        return self.__words

    def __addPlayedWords(self, word:str): #self
        self.__playedWords.append(word)
        return self
    def getPlayedWord(self): #array
        return self.__playedWords

    def __addScore(self, score:str): #self
        self.__score.append(int(score))
        return self
    def getScore(self): #array
        return self.__score
    
    def getMaxScore(self) -> int: #integer
        return min(self.__score)
    
    def setTour(self,tour:int): #self
        self.__tour = tour
        return self    
    def getTour(self): #integer
        return self.__tour
    
    def setCurrent(self, current): #Lself
        self.__current = current
        return self
    def getCurrent(self): #Word
        return self.__current
    
    def checkLetter(self,letter:str) -> str: #string
        """Permet de verifier que la lettre est dans le mot"""
        try:
            if not self.getCurrent().checkLetter(letter):
                self.setTour(self.getTour()+1)
        except Exception as error:
            return error
        
        return ''
    
    def start(self): #booleen
        """Call to start the game"""
        self.setCurrent(choice(self.getWords()))
        self.setTour(0)
        return True
        
    def end(self): #booleen
        """Call to end the game"""
        self.__addScore(self.getTour())
        self.__removeWords(self.getCurrent()).__addPlayedWords(self.getCurrent())
        return True
        
   
            