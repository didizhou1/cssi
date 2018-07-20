noun1 = input('Noun: ')
adjective1 = input('Adjective: ')
noun2 = input('Noun: ')
verb = input('-ing verb: ')

print('The {n} jumped over a {adj} {n2}. Then the {n2} decided to stop being so {adj} and take up a hobby: {v}').format(n = noun1, adj = adjective1, n2 = noun2, adj = adjective1, v = verb)
