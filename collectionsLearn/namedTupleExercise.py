from collections import namedtuple
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

Person = namedtuple("Person","name age gender orientation")
bob = Person("Bob Dylan", 45, "Male", "Straight")
susan = Person("Susan Sarandon", 23, "Female", "Gay")
kohli = Person("kohli", 45, "Male", "Straight")
sachin = Person("Sachin", 23, "Female", "Gay")
pp.pprint([bob,susan,kohli,sachin])

