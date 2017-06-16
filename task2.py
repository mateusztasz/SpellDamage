from collections import OrderedDict
from typing import List, Dict

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


def damage(spell: str) -> int:
    """
    Function calculating global damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage
    """
    result = list()

    # original order
    subspells = globalSubspells

    table_of_correations = [None, (1, 3), (2, 4), (2, 5), (0, 5), (0, 2)]
    # TODO table_of_correations = findCorrelations(subspells)

    # for each item in table of correalations, swap element and compute damage
    for elem in table_of_correations:
        if elem is not None:
            subspells = swap(subspells, elem[0], elem[1])
        result.append(run(spell, subspells))

    # return maximum value
    return max(result)


def run(spell: str, subspells: Dict[str, int]) -> int:
    """
    Function calculating local damage
    :param str spell: string with spell
    :param OrderedDict[str, int] subspells: subspells with damage
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


def swap(collection: dict, indexFirst: int, indexSecond: int) -> Dict:
    """
    Function swaping items in OrderedDict
    :param OrderedDict collection: dictionary with objects
    :param int indexFirst: index of first element to swap
    :param intindexSecond: index of second element to swap
    :rtype: OrderedDict
    :return: new dictionary with swapped elements
    """

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


def findCorelations(colection: dict) -> list:
    pass


if __name__ == '__main__':
    d = damage('feaineain')
    print(d)
