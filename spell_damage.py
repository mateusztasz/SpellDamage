from collections import OrderedDict

boundingSubspell = dict()
START = 'START'
END = "END"
boundingSubspell = {START:
                        {'spell': 'fe',
                         'value': 1},
                    END:
                        {'spell': 'ai',
                         'value': 2}}

globalSubspells = OrderedDict()
globalSubspells['dai'] = 5
globalSubspells['jee'] = 3
globalSubspells['ain'] = 3
globalSubspells['je'] = 2
globalSubspells['ne'] = 2
globalSubspells['ai'] = 2


def run(spell, subspells):
    """
    Function calculating damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage
    """
    result = 0
    # print("TEST: ", spell)
    spell = spell.strip()
    start = spell.find(boundingSubspell[START]['spell'])

    # no 'fe'
    if start == -1:
        return 0

    end = spell.rfind(boundingSubspell[END]['spell'])
    # 'no 'ai'
    if end == -1:
        return 0

    # 'ai' before 'fe'
    if start > end:
        return 0

    spell = spell[start + len(boundingSubspell[START]['spell']):end]

    # add points for 'fe' (+1) and 'ai' (+2)
    result += boundingSubspell[START]['value'] + boundingSubspell[END]['value']

    # multiple 'fe'
    if spell.find(boundingSubspell[START]['spell']) >= 0:
        return 0

    # the rest of spell - the inside to analyse
    startFindingFromBeginningKey = False
    for key in subspells.keys():

        if startFindingFromBeginningKey:
            key = list(subspells.keys())[0]
            startFindingFromBeginningKey = False

        start = spell.find(key)
        if start >= 0:
            spell = spell[0:start] + " " * len(key) + spell[start + len(key):]
            result += subspells[key]
            startFindingFromBeginningKey = True

    # subtract result by number of left letter
    for char in spell:
        if not char.isspace():
            result -= 1

    # negative damage
    if result < 0:
        return 0

    return result


def damage(spell):
    result = list()

    # original order
    subspells = globalSubspells
    result.append(run(spell, subspells))

    # je -> jee (zamiana)
    subspells = swap(subspells, 1, 3)
    result.append(run(spell, subspells))

    # ne -> ain (zamiana)
    subspells = swap(subspells, 2, 4)
    result.append(run(spell, subspells))

    # ai -> ain (zamiana)
    subspells = swap(subspells, 2, 5)
    result.append(run(spell, subspells))

    # ai -> dai
    subspells = swap(subspells, 0, 5)
    result.append(run(spell, subspells))

    # ain -> dai (zamiana)
    subspells = swap(subspells, 0, 2)
    result.append(run(spell, subspells))

    return max(result)


def swap(collection, indexFirst, indexSecond):
    keys = list(collection.keys())
    values = list(collection.values())

    newCollection = OrderedDict()
    for index in range(0, len(collection)):
        if index is indexFirst:
            newCollection[keys[indexSecond]] = values[indexSecond]
        elif index is indexSecond:
            newCollection[keys[indexFirst]] = values[indexFirst]
        else:
            newCollection[keys[index]] = values[index]

    return newCollection


def findCorelations(colection):
    pass


if __name__ == '__main__':
    d = damage('feaineain')
    print(d)
