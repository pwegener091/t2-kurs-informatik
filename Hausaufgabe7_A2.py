spielfeld = [
    ["O", "X", "O"],
    [" ", "X", "X"],
    ["X", "X", "O"]
]

x_won = False

# kontrollieren die Zeilen
for reihe in spielfeld:
    if reihe[0] == "X" and reihe[1] == "X" and reihe[2] == "X":
        x_won = True

#kontrollieren die Spalten
for i in range(3):
    if spielfeld[0][i] == "X" and spielfeld[1][i] == "X" and spielfeld[2][i] == "X":
        x_won = True

#kontrollieren die erste Diagonale
if spielfeld[0][0] == "X" and spielfeld[1][1] == "X" and spielfeld[2][2] == "X":
    x_won = True       

#kontrollieren die andere Diagonale
if spielfeld[0][2] == "X" and spielfeld[1][1] == "X" and spielfeld[2][0] == "X":
    x_won = True     

if x_won == True:
    print("Spieler X hat gewonnen.")
else:
    print("Spieler X hat nicht gewonnen.")
