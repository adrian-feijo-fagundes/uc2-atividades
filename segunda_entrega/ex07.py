nivel = 0
possui_cajado = True
possui_espada = False
if nivel >= 10 and (possui_cajado or possui_espada):
    print("Pode entrar na dungeon")
else:
    print("Ainda não possui nível ou equipamento necessário")