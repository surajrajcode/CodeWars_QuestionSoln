def list_(L):
    Lo = []
    Le = []
    for i in L:
        if i % 2 == 0:
            Lo.append(i)
        else:
            Le.append(i)
    if len(Lo) > len(Le):
        return Le[0]
    else:
        return Lo[0]