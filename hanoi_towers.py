def get_last(tower):
    if len(tower) == 0:
        return None
    return tower[len(tower) - 1]


def find_suitable_tower(source, towers=[]):
    next_tower = get_next_tower(source, towers)
    next_next_tower = get_next_tower(next_tower, towers)

    if len(towers[next_tower]) == 0:
        return next_tower
    if get_last(towers[source]) == get_last(towers[next_tower]) - 1:
        return next_tower
    if get_last(towers[next_tower]) - get_last(towers[source]) >= 3:
        return next_tower

    if len(towers[next_next_tower]) == 0:
        return next_next_tower
    if get_last(towers[source]) == get_last(towers[next_next_tower]) - 1:
        return next_next_tower
    if get_last(towers[next_next_tower]) - get_last(towers[source]) >= 3:
        return next_next_tower

    return -1


def get_next_tower(actual, towers):
    if actual == len(towers) - 1:
        return 0
    return actual + 1


def move_discs(n, moves=0, actual=0, last_move=0, towers=[]):
    if n == 1:
        destination = find_suitable_tower(actual, towers)
        if destination > -1:
            if last_move != get_last(towers[actual]):
                moves += 1
                last_move = towers[actual].pop()
                towers[destination].append(last_move)
        return moves, last_move, towers

    while len(towers[actual]) > 0:
        moves_before = moves
        moves, last_move, towers = move_discs(
            n - 1, moves, actual, last_move, towers)
        # nothing changed
        if moves == moves_before:
            next_tower = get_next_tower(actual, towers)
            if len(towers[next_tower]) > 0:
                moves, last_move, towers = move_discs(
                    n, moves, next_tower, last_move, towers)
            else:
                break

    return moves, last_move, towers


def move_tower(n, moves=0, actual=0, towers=[]):
    last_move = 0
    for i in range(len(towers)):
        if i > 0 and len(towers[i]) == n:
            return moves, towers
        if not (i > 0 and len(towers[i]) == 1 and get_last(towers[i]) == n):
            moves, last_move, towers = move_discs(
                n, moves, i, last_move, towers)

    return move_tower(n, moves, towers=towers)


def solve_puzzle(n):
    tower = []
    count = n
    while count > 0:
        tower.append(count)
        count -= 1

    print("Let's move those discs for N %s and stick #1 as %s" % (n, tower))
    moves, towers = move_tower(n, towers=[tower, [], []])
    print("Number of moves are %s and towers are: #1 %s #2 %s #3 %s" %
          (moves, towers[0], towers[1], towers[2]))


solve_puzzle(6)
