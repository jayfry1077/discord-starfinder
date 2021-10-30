import json
import requests
import traceback
from aws_lambda_powertools import Logger
from classes.data_lookup import Datalookup

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
    print(event)

    body = event['detail']

    lookup = Datalookup(body)

    try:
        update_message(body['application_id'], body['token'], lookup.lookup())
    except Exception as e:
        logger.error(e)
        logger.error(traceback.print_exception())
        update_message(body['application_id'], body['token'],
                       'Failed to lookup information')
