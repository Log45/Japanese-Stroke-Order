"""
Author: Logan Endes

stroke.py is a program for Japanese learners to remember the stroke order of 
different letters in hiragana and katakana. While it is not extremely accurate 
with regard to the exact shape of every letter, it it useful for remembering stroke
orders, something that I personally find myself struggling with. 
"""
from turtle import * 
from alphabets import alphabet


def draw_letter(letter: str, alphabet: str):
  """"""
  pensize(4)
  speed(2)
  if alphabet == "hiragana":
    if letter == "a":
      penup()
      goto(-60, 40)
      pendown()
      forward(60)
      penup()
      goto(-30, 60)
      pendown()
      right(90)
      forward(100)
      left(90)
      penup()
      goto(0, 10)
      pendown()
      right(90)
      circle(-50, 90)
      forward(5)
      right(90)
      circle(-40, 200)
    if letter == "i":
      penup()
      goto(-50, 30)
      pendown()
      setheading(250)
      forward(20)
      setheading(250)
      circle(50, 100)
      left(45)
      circle(30, 30)
      penup()
      goto(25, 25)
      setheading(315)
      pendown()
      circle(-100, 35)
    if letter == "u":
      penup()
      goto(-15, 35)
      pendown()
      setheading(330)
      forward(50)
      penup()
      goto(-25, -5)
      pendown()
      setheading(5)
      forward(40)
      right(60)
      circle(-40, 100)
      forward(20)
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
  