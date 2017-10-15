def correctPieces(firstPiece, secondPiece):
    aux = 0
    for i in firstPiece:
        for j in secondPiece:
            if i == j:
                aux = 1

    if aux == 1:
        return True
    else:
        return False




firstPiece = (3,4)
secondPiece = (5,6)

print(correctPieces(firstPiece, secondPiece))
