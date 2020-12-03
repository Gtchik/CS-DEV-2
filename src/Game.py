# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:42:17 2020

@author: gtchi
"""
from random import choice
from Word import *

class Game:
    nbTour=8
    def __init__(self, url):
        self.__playedWords=[]
        self.__score=[]
        self.__tour=0
        self.__current=''
        with open(url) as f:
            wordsList = f.read().splitlines()
            f.close()
        self.__words = [ Word(word) for word in wordsList]

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
    
    def setTour(self,tour): #self
        self.__tour = tour
        return self    
    def getTour(self): #integer
        return self.__tour
    
    def setCurrent(self, current):
        self.__current = current
        return self
    def getCurrent(self):
        return self.__current
    
    def checkLetter(self,letter):
        try:
            self.getCurrent().checkLetter(letter)
        except Exception as error:
            return error
        self.setTour(self.getTour()+1)
        return ''
    
    def start(self):
        self.setCurrent(choice(self.getWords()))
        self.setTour(0)
        return True
        
    def end(self):
        self.__addScore(self.getTour())
        self.__removeWords(self.getCurrent()).__addPlayedWords(self.getCurrent())
        return True
        
   
            