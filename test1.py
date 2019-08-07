from boot import BattleBot,Arena,BattleBot2
Bot1 = BattleBot("Sil3nt")
Bot2 = BattleBot2("R2D2")
arena = Arena(Bot1, Bot2)


print(Bot1.name)
print(Bot2.name)
arena.battle()

