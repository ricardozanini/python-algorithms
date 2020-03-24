def get_last(tower):
    if len(tower) == 0:
        return None
    return tower[len(tower) - 1]


def find_suitable_tower(source, last_move, towers=[]):
    if get_last(towers[source]) == last_move:
        return -1

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


def move_discs(moves=0, actual=0, last_move=0, towers=[]):
    while len(towers[actual]) > 0:
        destination = find_suitable_tower(actual, last_move, towers)
        if destination > -1: # we've found a possible movement for this tower
            moves += 1
            last_move = towers[actual].pop()
            towers[destination].append(last_move)
        else:  # nothing changed, let's try to clean up the next tower
            next_tower = get_next_tower(actual, towers)
            # emptying the next tower, this way we can have some room to arrange our discs
            if len(towers[next_tower]) > 0:
                moves, last_move, towers = move_discs(
                    moves, next_tower, last_move, towers)
            else: # no way out, we did what we could, this tower has no movements left
                break

    return moves, last_move, towers


def move_tower(n, moves=0, towers=[]):
    last_move = 0
    for i in range(len(towers)):
        # break the loop once we got the solution
        if i > 0 and len(towers[i]) == n:
            return moves, towers
        # keep trying to move the discs from the current tower
        moves, last_move, towers = move_discs(moves, i, last_move, towers)

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
