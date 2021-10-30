import json
import requests


def data_by_title(data_list=[dict], filename=str):
    with open(f'{filename}.json', 'w') as f:
        f.write(json.dumps(
            {str(data['title']).lower(): data for data in data_list}))


def spell_details(spell_title=str, detail=None) -> dict:

    spells = json.load(open('spell_by_spell_title.json',
                            encoding='utf-8'))

    x = spells[spell_title]

    if detail != None:
        print(x[detail])
        return

    print(spells[spell_title])


# spell_details('Animate Dead', 'school')

def make_options(keys=dict):
    data = [{"name": "All", "value": "ALL"}]

    for key in keys.keys():
        data.append(
            {
                "name": key,
                "value": key,
            })

    return json.dumps(data)


def paginate_data(url=str):

    data = []
    response = json.loads(requests.get(f'{url}').content)

    data += response['results']

    while response['next'] != None:
        response = json.loads(requests.get(response['next']).content)
        data += response['results']

    return data


api_urls = {
    "weapons": "https://api.starfinder.dragonlash.com/weapons/",
    "armors": "https://api.starfinder.dragonlash.com/armors/",
    "spells": "https://api.starfinder.dragonlash.com/spells/",
    "abilities": "https://api.starfinder.dragonlash.com/abilities/",
    "creatures": "https://api.starfinder.dragonlash.com/creatures/"
}

# for key, value in api_urls.items():
#     data_by_title(paginate_data(value), f'{key}_by_{key}_title')

# for key, value in api_urls.items():
#     data = json.load(open(f'{key}_by_{key}_title.json', encoding='utf-8'))
#     for data_key, data_value in data.items():
#         print(f'********{key}********')
#         print(make_options(data_value))
#         print(f'****************')
#         break
