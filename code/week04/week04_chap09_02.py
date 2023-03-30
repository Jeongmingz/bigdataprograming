def buggy(arg, result=[]):
    result.append(arg)
    print(result)


def works(arg):
    result = [arg]
    return result


def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


buggy('a')
buggy('b')

print(works('a'), works('b'), sep='\n')

nonbuggy('a')
nonbuggy('b')
