import json
import requests
from aws_lambda_powertools import Logger

logger = Logger(service='starfinder-lookup')


def update_message(application_id=str, token=str, message=str):
    url = 'https://discord.com/api/webhooks/{application_id}/{token}/messages/@original'.format(
        application_id=application_id, token=token)
    payload = {'content': message}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(url=url, headers=headers,
                              data=json.dumps(payload)).json()
    logger.info(response)
    return


def main(event, context):

    body = event['detail']

    update_message(body['application_id'], body['token'],
                   f'Test Successful.')
