# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:20:58 2021

@author: qinan
"""
import hangman
secret_word = 'apple'
print(hangman.match_with_gaps("app_ e", secret_word))
# word = " app_ e "
# word = word.strip(' ')
# print(word)
hangman.show_possible_matches("a_ _ c")