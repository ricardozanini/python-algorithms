
def sequence():
    source = [0,1,2,3,4,5]
    destin = [1,3,2,0,5,4]
    result = []
    for i in range(len(source)):
        if source[i] != destin[i]:
            for j in range(i, len(source)):
                if source[j] == destin[i]:
                    result.append((i, j))
                    break
    return result

print(sequence())