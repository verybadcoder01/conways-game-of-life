
configs = [{}]
states = [[[]]]


def equals(a, b):
    if len(a) != len(b):
        return 0
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            if a[i][j].alive != b[i][j].alive:
                return 0
    return 1


def check_evolution(field, iterations: int):
    if len(states) == 1:
        return 1
    for i in range(0, len(states)):
        for j in range(0, len(states)):
            if equals(states[i], states[j]) and i != j:
                configs.append({iterations: field})
                print("EVOLUTION FINISHED")
                return 0
    for i in states[-1]:
        for j in i:
            if j.alive == 1:
                return 1
    configs.append({iterations: field})
    print("EVOLUTION FINISHED")
    return 0
