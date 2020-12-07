# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:42:17 2020

@author: gtchi
"""

class Word:
    def __init__(self,word):
        # Contains the letters already entered
        self.__letters = [word[0]]
        # Contains the tour number
        self.__word = word
                
    def __setWord(self, word=str()): #self
        self.__word = word
        return self
    def getWord(self):#string
        return self.__word
 
    def getHiddenWord(self): #string
        hiddenWord = ''
        for val in self.getWord():
            if val in self.getLetters():
                hiddenWord += val
            else:
                hiddenWord += '_'            
        return hiddenWord
    
    def __addLetter(self, letter=str()): #self
        self.__letters.append(letter)
        return self
    def getLetters(self): #array
        return self.__letters
    
    def checkLetter(self,letter=str()): #booleen
        """Use to check letter (deja joue, plusieur caractere, dans le mot)"""
        letter = letter.lower()
        if len(letter)!=1:
            raise Exception('Une seule lettre est attendu')
        if letter in self.getLetters():
            raise Exception('Lettre déjà jouée')
        self.__addLetter(letter)
        if letter in self.getWord():
            return True
        return False