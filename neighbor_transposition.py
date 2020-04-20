
def sequence():
    source = [0, 1, 2, 3, 4, 5]  # MARINE
    destin = [1, 3, 2, 0, 5, 4]  # AIRMEN
    result = []
    for i in range(len(source)):
        if source[i] != destin[i]:
            for j in range(i, len(source)):
                if source[j] == destin[i]:
                    for k in range(j, i, -1):
                        left = source[k-1]
                        right = source[k]
                        source[k-1] = right
                        source[k] = left
                        result.append((k-1, k))
                    break
    return result


print(sequence())
