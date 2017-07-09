# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:27:36 2017

@author: ritzzeee
"""
#%%
import random

def menu_choice():
    print("do you want to roll die?")
    ch=input("choice(y/n):")
    if (ch=='y'):
        roll_die()
    else:
        if (ch=='n'):
            print("quitiing")
            
            
def roll_die():
    print(random.randint(1,6))
    menu_choice()
