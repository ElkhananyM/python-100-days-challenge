# from turtle import Turtle, Screen
#
# kuku = Turtle()
# my_screen = Screen()
#
# kuku.shape("turtle")
# kuku.color("DarkOrchid1")
# kuku.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)