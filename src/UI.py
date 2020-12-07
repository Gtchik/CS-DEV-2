# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:47:22 2020
@Tp-2
@author: gtchi
"""
from Game import Game
from tkinter import Tk, PhotoImage, StringVar, Label, Button, Entry, Frame



class UI:
    def __init__(self,game):
        self.__game = game
        #Creation de la fenetre
        self.__root = Tk()
        self.__root.title('Jeu du pendu')
        #defintion des variable
        self.__imgs=[PhotoImage(file=f"../data/img/bonhomme{9-i}.gif") for i in range(1,9)]
        self.__letter = StringVar()
        self.__hiddenword = StringVar()
        self.__error = StringVar()
    def getGame(self):
        return self.__game
    
    
        
    def start(self):
        """Tkinter game"""
    
        
        def replay(message,message2=''):
            def restart():
                replay.destroy()
                self.__root = Tk()
                self.__root.title('Jeu du pendu')
                self.start()
            game.end()
            replay = Tk()
            Label(replay, text= message).pack(side = 'top')
            Label(replay, text= message2).pack(side = 'top')
            replay.title('Voulez vous rejouer')
            Label(replay, text='Voulez vous rejouez ?').pack(side = 'top')
            Button(replay, bg='grey', text = 'Oui' ,command = restart).pack(side = 'bottom')
            Button(replay, bg='grey', text = 'Non' ,command = replay.destroy).pack(side = 'bottom')
            replay.mainloop()
     
        def verification():
            #verifie la lettre et affiche le message
            self.__error.set(game.checkLetter(self.__letter.get()))
            self.__letter.set('') #reinitialisation de l'entry
            self.__hiddenword.set(game.getCurrent().getHiddenWord())#modification du mot
            #modification de l'image
            image.configure(image=self.__imgs[game.getTour()])
            #image.image=img2 #permet de ne pas faire disparaitre img2 par GC (GarbageCollect)
            
            #verification des fin de partie
            if game.getCurrent().getHiddenWord()==game.getCurrent().getWord():
                self.__root.destroy()
                replay('victoire!')
            if game.getTour()>=game.nbTour:
                self.__root.destroy()
                replay('Perdu...', "Le mot etait "+game.getCurrent().getWord())
    
        #Initialisation du jeu    
        game = self.getGame()
        game.start()
        
        
        
        #Remise à 0 des variables
        self.__hiddenword.set(game.getCurrent().getHiddenWord())
        self.__letter.set('')
        self.__error.set('')
        
        
        #creation de ma frame
        Frame1 = Frame(self.__root)
        Frame1.pack()
        
        #contenu de ma fenetre
        Button(Frame1, bg='grey', text = 'Quitter' ,command = self.__root.destroy).pack(side = 'bottom')
        Label(Frame1, textvariable = self.__hiddenword).pack(side = 'left')
        Entry(Frame1, textvariable = self.__letter).pack(side = 'left')
        Label(Frame1, textvariable = self.__error).pack(side = 'left')
        Button(Frame1, text ='PROPOSER', command = verification).pack(side='left')
        image = Label(Frame1, image=self.__imgs[0])
        image.pack()
        
        self.__root.mainloop()
        
if __name__ == '__main__':
    UI(Game('Words.txt')).start()

