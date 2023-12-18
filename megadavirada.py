from random import randint

games = []
games.append([30, 46, 53, 56, 59, 60])
games.append([22, 33, 35, 39, 50, 54])
games.append([18, 35, 36, 56, 58, 59])
games.append([13, 24, 33, 43, 51, 60])
games.append([2, 5, 29, 30, 45, 48])
games.append([4, 7, 10, 23, 28, 57])
games.append([1, 6, 7, 8, 18, 52])

winner_game = []
#for i in range(0, 6):
#    while True:
#        rand = randint(1, 60)
#        if not rand in winner_game:
#            break
#    winner_game.append(rand)

winner_game = [17, 20, 22, 35, 41, 42]
winner_game = sorted(winner_game)


print("""
      WINNER GAME
      {0} - {1} - {2} - {3} - {4} - {5}
      """.format(winner_game[0],
                winner_game[1],
                winner_game[2],
                winner_game[3],
                winner_game[4],
                winner_game[5]))


matching_count = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}

for game in games:

    matching_numbers = len(list(set(winner_game) & set(game)))
    matching_count[matching_numbers] += 1

some_money = False

if matching_count[6] > 0:
    print("""
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            ESTAMOS MILIONÁRIOS
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """)
    some_money = True

if matching_count[5] > 0:
    print("""
    =====================================
        GANHAMOS A QUINA!!
    =====================================
    """)
    some_money = True

if matching_count[4] > 0:
    print("""
    =====================================
        GANHAMOS A QUADRA!!
    =====================================
    """)
    some_money = True

if not some_money:
    print("""
    =====================================
        ganhamos porra nenhuma =/
    =====================================
    """)

print("""
        fizemos {0} jogos: \n
        {1} acertamos nenhuma
        {2} acertamos uma
        {3} acertamos duas
        {4} acertamos três
        {5} acertamos a quadra
        {6} acertamos a quina
        {7} acertamos a sena
    """.format(str(len(games)),
               str(matching_count[0]),
               str(matching_count[1]),
               str(matching_count[2]),
               str(matching_count[3]),
               str(matching_count[4]),
               str(matching_count[5]),
               str(matching_count[6]),
       ))

