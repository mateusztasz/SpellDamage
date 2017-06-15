from collections import OrderedDict

START = 'fe'
END = 'ai'


def run(spell, subspells):
    """
    Function calculating damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage
    """
    result = 0
    print("TEST: ", spell)
    spell = spell.strip()
    start = spell.find(START)

    # no 'fe'
    if start == -1:
        return 0

    end = spell.rfind(END)
    # 'no 'ai'
    if end == -1:
        return 0

    # 'ai' before 'fe'
    if start > end:
        return 0

    spell = spell[start + len(START):end]

    # add points for 'fe' (+1) and 'ai' (+2)
    result += 3

    # multiple 'fe'
    if spell.find(START) >= 0:
        return 0

    # the rest of spell - the inside to analyse
    print('spell :', spell)
    cont = False
    for key in subspells.keys():

        if cont:
            key = list(subspells.keys())[0]
            cont = False

        print("SZUKAM: ", key)
        start = spell.find(key)
        if start >= 0:
            print('FOUND KEY: ', key)
            #print('POCZATEK:', spell[0:start], 'start:', start)
            #print('KONIEC:', spell[start + len(key):])
            #spell = spell[0:start] + spell[start + len(key):]
            spell = spell[0:start] + " "*len(key) + spell[start + len(key):]
            result += subspells[key]

            cont = True

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
    subspells = OrderedDict()

    # original order
    subspells['dai'] = 5
    subspells['jee'] = 3
    subspells['ain'] = 3
    subspells['je'] = 2
    subspells['ne'] = 2
    subspells['ai'] = 2
    result.append(run(spell, subspells))

    subspells = OrderedDict()
    # je -> jee (zamiana)
    subspells['dai'] = 5
    subspells['je'] = 2
    subspells['ain'] = 3
    subspells['jee'] = 3
    subspells['ne'] = 2
    subspells['ai'] = 2
    result.append(run(spell, subspells))

    subspells = OrderedDict()
    # ne -> ain (zamiana)
    subspells['dai'] = 5
    subspells['jee'] = 3
    subspells['ne'] = 2

    subspells['je'] = 2
    subspells['ain'] = 3
    subspells['ai'] = 2
    result.append(run(spell, subspells))

    subspells = OrderedDict()
    # ai -> ain (zamiana)
    subspells['dai'] = 5
    subspells['jee'] = 3
    subspells['ai'] = 2

    subspells['je'] = 2
    subspells['ne'] = 2
    subspells['ain'] = 3
    result.append(run(spell, subspells))

    subspells = OrderedDict()
    # ai -> dai

    subspells['ai'] = 2
    subspells['jee'] = 3
    subspells['ain'] = 3
    subspells['je'] = 2
    subspells['ne'] = 2
    subspells['dai'] = 5
    result.append(run(spell, subspells))

    subspells = OrderedDict()
    # ain -> dai (zamiana)
    subspells['ain'] = 3
    subspells['jee'] = 3
    subspells['dai'] = 5

    subspells['je'] = 2
    subspells['ne'] = 2
    subspells['ai'] = 2
    result.append(run(spell, subspells))

    return max(result)


if __name__ == '__main__':
    d = damage('feaineain')
    print(d)
'''
  subspells = OrderedDict()

  subspells['dai'] = 5
  subspells['jee'] = 3
  subspells['ai'] = 2

  subspells['je'] = 2
  subspells['ne'] = 2
  subspells['ain'] = 3
  r= run("feaineai")
  print(r)
  '''
