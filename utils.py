import json


def spell_by_spell_title(spells):
    file = open('spell_by_spell_title.json', 'w')
    file.write(json.dumps(
        {spell['title']: spell for spell in spells}))
    file.close()


# spell_by_spell_title(
#     json.load(open('starfinder_spells.json', encoding='utf-8'))['spells'])


def spell_details(spell_title=str, detail=None) -> dict:

    spells = json.load(open('spell_by_spell_title.json',
                            encoding='utf-8'))

    x = spells[spell_title]

    if detail != None:
        print(x[detail])
        return

    print(spells[spell_title])


spell_details('Animate Dead', 'school')
