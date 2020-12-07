# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:06:36 2020
@Tp-2
@author: gtchi
"""

from UI import UI
from ConsoleUI import ConsoleUI

"""
Lire le readme !
"""

if __name__ == '__main__':
    if input("Voulez vous jouez en mode graphique (Tkinter) ? (y/N): ")=="N":
        ConsoleUI(Game('Words.txt')).start()
    else:
        UI(Game('Words.txt')).start()

