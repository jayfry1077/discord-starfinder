import json


class Datalookup():
    def __init__(self, event) -> None:
        self.options = event['data']['options']
        self.command = self.options[0]['name']

    def get_seralizer(self):
        if self.command == 'spell':
            return self.spell_seralizer
        elif self.command == 'ability':
            return self.ability_seralizer
        elif self.command == 'weapon':
            return self.weapon_seralizer
        elif self.command == 'armor':
            return self.armor_seralizer
        elif self.command == 'creature':
            return self.creature_seralizer

    def __get_data(self, file_name):

        data = json.load(open(f'./data/{file_name}.json', encoding='utf-8'))

        op_by_op_name = {
            option['name']: option for option in self.options[0]['options']}

        title = op_by_op_name['title']['value'].lower()
        attribute = op_by_op_name['attributes']['value']

        if attribute == 'ALL':
            return self.__format_message(data[title])
        else:
            try:
                return f'```{data[title][attribute]}```'
            except:
                return f'```{self.command} not found.```'

    def __format_message(self, data=dict):

        start_message = '```'

        for key, value in data.items():

            start_message += f'{key}: {value}' + '\n'

        end_message = f'{start_message}```'

        return end_message

    def spell_seralizer(self):
        spell_data = self.__get_data('spells_by_spells_title')

        return spell_data

    def weapon_seralizer(self):
        weapon_data = self.__get_data('weapons_by_weapons_title')

        return weapon_data

    def armor_seralizer(self):
        armor_data = self.__get_data('armors_by_armors_title')

        return armor_data

    def ability_seralizer(self):
        ability_data = self.__get_data('abilities_by_abilities_title')

        return ability_data

    def creature_seralizer(self):
        creature_data = self.__get_data('creatures_by_creatures_title')

        return creature_data

    def lookup(self):

        searlizer = self.get_seralizer()

        return searlizer()
