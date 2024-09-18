def puissance_rec(nombre, puissance):
    if not puissance:
        return 1
    elif not puissance % 2:
        return puissance_rec(nombre, int(puissance / 2)) \
        * puissance_rec(nombre, int(puissance / 2))
    else:
        return nombre * puissance_rec(nombre, puissance - 1)