import pygame
class battleSystem:
    def __init__(self):
        self.count = 0

    def attackFunctions(self,pokemon):
        self.pokemon = pokemon
        for i in range(0,len(pokemon.moves)):
            print(pokemon.moves[i].name)
        self.choice = int(input("please input which move you want to do "))
        self.moves = pokemon.moves[self.choice]
        if self.moves.moveLeft <= 0:
            print("out of moves sir ")
            self.attackFunctions(pokemon)
        else:
            pokemon.moves[self.choice].movesLeft -= 1
            return self.moves

    def speedsorter(self,pokemonList):
        sorted(pokemonList.speed)

    def attackPhase(self,move, pokemonAttacking,pokemonDefending):
        self.pokemonAttacking = pokemonAttacking
        pokemonDefending.HP -= move.damage
        if pokemonDefending.HP <=0:
            return print("Game ends")

