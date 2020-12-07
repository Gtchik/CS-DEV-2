# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:47:22 2020

@author: gtchi
"""
from Game import *
from tkinter import *

class UI:
    def __init__(self,game):
        self.__game = game
    def getGame(self):
        return self.__game
    
    def consoleStart(self):
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
            
    def tkinterStart(self):
        """Tkinter game"""
        def replay(message,message2=''):
            game.end()
            replay = Tk()
            Label(replay, text= message).pack(side = 'top')
            Label(replay, text= message2).pack(side = 'top')
            replay.title('Voulez vous rejouer')
            Label(replay, text='Voulez vous rejouez ?').pack(side = 'top')
            Button(replay, bg='grey', text = 'Oui' ,command = self.tkinterStart).pack(side = 'bottom')
            Button(replay, bg='grey', text = 'Non' ,command = replay.destroy).pack(side = 'bottom')
            replay.mainloop()
     
        def verification():
            #verifie la lettre et affiche le message
            erreur.set(game.checkLetter(letter.get()))
            letter.set('') #reinitialisation de l'entry
            hiddenword.set(game.getCurrent().getHiddenWord())#modification du mot
            #modification de l'image
            img2 = PhotoImage(file="../data/img/bonhomme"+str(game.nbTour+1-game.getTour())+".gif")
            image.configure(image=img2)
            image.image=img2
            
            #verification des fin de partie
            if game.getCurrent().getHiddenWord()==game.getCurrent().getWord():
                root.destroy()
                replay('victoire!')
            if game.getTour()>=game.nbTour:
                root.destroy()
                replay('Perdu...', "Le mot etait "+game.getCurrent().getWord())
    
        #Initialisation du jeu    
        game = self.getGame()
        game.start()
        
        #Creation de la fenetre
        root = Tk()
        root.title('Jeu du pendu')
        
        #Creation des variables
        hiddenword = StringVar()
        hiddenword.set(game.getCurrent().getHiddenWord())
        letter = StringVar()
        erreur = StringVar()
        erreur.set('')
        img = PhotoImage(file="../data/img/bonhomme8.gif")
        
        #creation de ma frame
        Frame1 = Frame(root)
        Frame1.pack()
        
        #contenu de ma fenetre
        Button(Frame1, bg='grey', text = 'Quitter' ,command = root.destroy).pack(side = 'bottom')
        Label(Frame1, textvariable = hiddenword).pack(side = 'left')
        Entry(Frame1, textvariable = letter).pack(side = 'left')
        Label(Frame1, textvariable = error).pack(side = 'left')
        Button(Frame1, text ='Check', command = verification).pack(side='left')
        image = Label(Frame1, image=img)
        image.pack()
        
        root.mainloop()
        
if __name__ == '__main__':
    UI(Game('Words.txt')).tkinterStart()

