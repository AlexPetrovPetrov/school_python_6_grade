# for loop
# for i in range(10):
#     print("Hello world",i)
# animals = ["cat","dog","caw","monkey","snake"]
# for animal in animals:
#     print("I like a ",animal)
# word = "Hello"

# reverse_word = ""

# for letter in word:
#     print(letter)
#     if letter == "l":
#         reverse_word = "x" + reverse_word
#     else: 
#         reverse_word = letter + letter + reverse_word
# print(reverse_word)
# word = "wwoqioqi"
# counter = 0
# for letter in word:
#     if letter == "e":
#         counter = 1 + counter
# print("The word "+ word + " contains "+ str(counter) + " times letter e.")
    

from turtle import *
alex = Turtle()
screen = Screen()
alex.color("red")
goto(0,0)
shape = 50
shape_length = 30
alex.fillcolor("red")
alex.begin_fill()
for pen in range(shape):
    alex.forward(shape_length)
    alex.left(360/shape)
alex.end_fill()

screen.exitonclick()
