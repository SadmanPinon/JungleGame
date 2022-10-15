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


riverAreas = [
            (3,1),(3,2),(3,4),(3,5),
            (4,1),(4,2),(4,4),(4,5),
            (5,1),(5,2),(5,4),(5,5)
            ]
trapAreas = [
    (0,2),(8,2),
    (0,4),(8,4),
    (1,3),(7,3)
    ]

denAreas = [(0,3),(8,3)]