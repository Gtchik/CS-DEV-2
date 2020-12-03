# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:42:58 2020

@author: gtchi
"""
import unittest
import sys
sys.path.insert(1, '../src')
from Word import *

class WordTest(unittest.TestCase):
    
    def setUp(self):
        self.word = Word('envie')
    
    def test_word(self):
        response = self.word.getWord()
        self.assertEqual(response, 'envie')
    
    def test_current(self):
        current = self.word.getHiddenWord()
        self.assertEqual(current, 'e___e')
        
    def test_getLetter(self):
        self.word.checkLetter('r')
        self.word.checkLetter('u')
        self.word.checkLetter('x')
        letters = self.word.getLetters()
        self.assertEqual(letters.sort(), ['e','r','u'].sort())
        
    def test_victoire(self):
        self.word.checkLetter('n')
        self.word.checkLetter('v')
        self.word.checkLetter('i')
        current = self.word.getHiddenWord()
        self.assertEqual(current, 'envie')
    
    def test_maj_min(self):
        self.word.checkLetter('N')
        self.word.checkLetter('X')
        self.word.checkLetter('i')
        self.word.checkLetter('V')
        current = self.word.getHiddenWord()
        self.assertEqual(current, 'envie')    
        
    def test_doubleLetters(self):
        self.word.checkLetter('x')
        with self.assertRaises(Exception):
            self.word.checkLetter('x')
            
    def test_multipleLetters(self):
        with self.assertRaises(Exception):
            self.word.checkLetter('xg')
        
if __name__ == '__main__':
    unittest.main()