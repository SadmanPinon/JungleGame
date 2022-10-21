from enum import Enum

class Player(Enum):
    One = 1
    Two = 2
    
class SquareType(Enum):
    Normal = 1
    Water = 2
    Trap = 3
    Den  = 4

class PieceType(Enum):
    Rat = 1
    Cat = 2
    Dog = 3
    Wolf = 4
    Leopard = 5
    Tiger = 6
    Lion = 7
    Elephant = 8

columnDict = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    "D" : 3,
    'E': 4,
    'F' : 5,
    'G' : 6
}

#Mapping of Starting ( Origin) and Jump Destinations 
jumpPoints = [
    [(3,0),(3,3)],
    [(4,0),(4,3)],
    [(5,0),(5,3)],
    [(2,1),(6,1)],
    [(2,2),(6,2)],
    [(3,3),(3,6)],
    [(4,3),(4,6)],
    [(5,3),(5,6)],
    [(6,4),(2,4)],
    [(6,5),(2,5)],
]  

#Coordinates of the Squares that make up the River
riverAreas = [
            (3,1),(3,2),(3,4),(3,5),
            (4,1),(4,2),(4,4),(4,5),
            (5,1),(5,2),(5,4),(5,5)
            ]

#Coordinates of the Squares that make up the Traps
trapAreas = [
    (0,2),(8,2),
    (0,4),(8,4),
    (1,3),(7,3)
    ]

#Coordinates of the Squares that make up the Den
denAreas = [(0,3),(8,3)]