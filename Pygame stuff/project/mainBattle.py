import pygame
from pokemon import pokemon
from moves import moves
from battlesystem import battleSystem
moveList = []
moveList.append(moves("fire",75,5))
moveList.append(moves("earth",100,0))
moveList.append(moves("wind",50,50))
moveList.append(moves("water",10,100))

pokemonA = pokemon("laaron",200,moveList,100)
pokemonB = pokemon("laaron",200,moveList,100)

while True:
    battleSystem = battleSystem()
    move = battleSystem.attackFunctions(pokemonA)
    battleSystem.attackPhase(move,pokemonA,pokemonB)
    print(pokemonB.HP)
