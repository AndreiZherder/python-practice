# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
# и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
# Sample Input:
#
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
#
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
win_result = {'games': 1, 'wins': 1, 'draws': 0, 'looses': 0, 'points': 3}
loose_result = {'games': 1, 'wins': 0, 'draws': 0, 'looses': 1, 'points': 0}
draw_result = {'games': 1, 'wins': 0, 'draws': 1, 'looses': 0, 'points': 1}
tournament = {}
games = int(input())
for _ in range(games):
    team1, score1, team2, score2 = input().split(';')
    if int(score1) > int(score2):
        team1_result = win_result
        team2_result = loose_result
    elif int(score2) > int(score1):
        team1_result = loose_result
        team2_result = win_result
    else:
        team1_result = draw_result
        team2_result = draw_result
    if team1 in tournament:
        tournament[team1]['games'] += team1_result['games']
        tournament[team1]['wins'] += team1_result['wins']
        tournament[team1]['draws'] += team1_result['draws']
        tournament[team1]['looses'] += team1_result['looses']
        tournament[team1]['points'] += team1_result['points']
    else:
        tournament[team1] = team1_result.copy()
    if team2 in tournament:
        tournament[team2]['games'] += team2_result['games']
        tournament[team2]['wins'] += team2_result['wins']
        tournament[team2]['draws'] += team2_result['draws']
        tournament[team2]['looses'] += team2_result['looses']
        tournament[team2]['points'] += team2_result['points']
    else:
        tournament[team2] = team2_result.copy()
for team, result in tournament.items():
    print(f'{team}:{" ".join(str(i) for i in list(result.values()))}')
