class Datalookup():
    def __init__(self, event) -> None:
        self.options = event['detail']['data']['options']


test = {'detail': {
        'application_id': '',
        'channel_id': '',
        'data': {
            'id': '',
            'name': 'lookup',
                    'options': [{
                        'name': 'spell',
                                'options': [{
                                    'name': 'title',
                                    'type': 3,
                                    'value': 'hmm'
                                }, {
                                    'name': 'attributes',
                                    'type': 3,
                                    'value': 'level_requirements'
                                }],
                        'type': 1
                    }],
            'type': 1
        }}
