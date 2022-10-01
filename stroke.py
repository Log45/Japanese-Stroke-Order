"""
Author: Logan Endes

stroke.py is a program for Japanese learners to remember the stroke order of 
different letters in hiragana and katakana. While it is not extremely accurate 
with regard to the exact shape of every letter, it it useful for remembering stroke
orders, something that I personally find myself struggling with. 
"""
from turtle import * 
from alphabets import alphabet
from functions import *
from playsound import playsound



#playsound("samurai.mp3")
def draw_letter(letter: str, alphabet: str):
  """"""
  pensize(4)
  speed(2)
  if alphabet == "hiragana":
    if letter == "a":
      a_hir_turtle()
    if letter == "i":
      i_hir_turtle()
    if letter == "u":
      u_hir_turtle()
    if letter == "e":
      e_hir_turtle()
    if letter == "n":
      n_hir_turtle()
  elif alphabet == "katakana":
    pass
  else:
    print("Error: Invalid Alphabet.\n Input should be either 'hiragana' or 'katakana'.")


def main():
  """"""
  letter = input("What letter are you writing? ")
  alph = input("Which alphabet are you writing?(hiragana/katakana) ")
  for i in alphabet:
    if letter == i:
      draw_letter(i, alph)


def test():
  for i in alphabet:
    draw_letter(i, "hiragana")
    clear()
  for i in alphabet:
    draw_letter(i, "katakana")
    clear()


if __name__ == "__main__":
  test()
  done()
  