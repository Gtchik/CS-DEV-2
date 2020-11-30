# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:42:17 2020

@author: gtchi
"""

class Word:
    def __init__(self):
        # Contains the word to guess
        self.__word = ''
        # Contains the letters already entered
        self.__letters = []
        # Contains the current status of the displayed word
        self.__current = ''
        # Contains the tour number
        self.__tour = 0
        
    def setWord(self, word): #self
         self.__word = word
         self.__setCurrent(''.join([word[0]]+['_' for _ in range(1,len(word))]))
         return self
    def getWord(self):#string
        return self.__word
    
    def __setCurrent(self, current): #self
        self.__current = current
        return self
    def getCurrent(self): #string
        return self.__current
    
    def __addLetter(self, letter): #self
        self.__letters.append(letter)
        return self
    def getLetters(self): #array
        return self.__letters
    
    def setTour(self,tour): #self
        self.__tour = tour
        return self    
    def getTour(self): #integer
        return self.__tour
    
    def __convertLetter(self,letter): #string
        x='AZERTYUIOPQSDFGHJKLMWXCVBNàäâéèêëîïöôûü'
        y='azertyuiopqsdfghjklmwxcvbnaaeeeeeiioouu'
        mytable = letter.maketrans(x, y);
        return letter.translate(mytable)

    
    def __isLetter(self,letter): #array
        index = []
        for i, val in enumerate(self.getWord()):
            if val==letter:
                index.append(i)
        return index
    
    def checkLetter(self,letter): #array
        if self.getTour()>=8:
            return [False, 'Game Over', False]
        letter = self.__convertLetter(letter)
        if len(letter)!=1:
            return [False, 'Une seule lettre est attendu', True]
        if letter in self.getLetters():
            return [False, 'Lettre déjà jouée', True]
        self.setTour(self.getTour()+1)
        for i, val in enumerate(self.__isLetter(letter)):
            self.__addLetter(letter)
            self.__setCurrent(self.__current[:val]+letter+self.__current[val+1:])
        if self.getCurrent()==self.getWord():
            return [False, 'Victoire !', False]
        return [True]