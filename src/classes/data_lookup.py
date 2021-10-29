import json


class Datalookup():
    def __init__(self, event) -> None:
        self.options = event['data']['options']

    def get_seralizer(self):

        command = self.options[0]['name']

        if command == 'spell':
            return self.spell_seralizer
        elif command == 'ability':
            return self.ability_seralizer
        elif command == 'weapon':
            return self.weapon_seralizer
        elif command == 'armor':
            return self.armor_seralizer
        elif command == 'creature':
            return self.creature_seralizer

    def __get_data(self, file_name):

        data = json.load(open(f'./data/{file_name}.json', encoding='utf-8'))

        op_by_op_name = {
            option['name']: option for option in self.options[0]['options']}

        title = op_by_op_name['title']['value']
        attribute = op_by_op_name['attributes']['value']

        if attribute == 'ALL':
            return json.dumps(data[title])
        else:
            return json.dumps(data[title][attribute])

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

        # test = {'detail': {
        #         'application_id': '',
        #         'channel_id': '',
        #         'data': {
        #             'id': '',
        #             'name': 'lookup',
        #                     'options': [{
        #                         'name': 'spell',
        #                                 'options': [{
        #                                     'name': 'title',
        #                                     'type': 3,
        #                                     'value': 'hmm'
        #                                 }, {
        #                                     'name': 'attributes',
        #                                     'type': 3,
        #                                     'value': 'level_requirements'
        #                                 }],
        #                         'type': 1
        #                     }],
        #             'type': 1
        #         }}
