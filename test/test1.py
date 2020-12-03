# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:42:58 2020

@author: gtchi
"""

import random
import unittest

class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, liste)