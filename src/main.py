import json
import boto3
import os
from discord_funcs import valid_signature, discord_body
from aws_lambda_powertools import Logger


DISCORD_PING_PONG = {'statusCode': 200, 'body': json.dumps({"type": 1})}

STAGE = os.environ.get('STAGE', 'dev')
EVENT_BUS = f'discord-starfinder-{STAGE}'
logger = Logger(service='invoke')

event_bridge = boto3.client('events')


def send_event_bridge_event(event_body):

    source = f"discord.{event_body['data']['name']}"

    event = [{
        'Source': source,
        'DetailType': 'discord',
        'Detail': json.dumps(event_body),
        'EventBusName': EVENT_BUS
    }]
    try:
        event_bridge.put_events(Entries=event)
    except Exception as e:
        logger.error(e)


def main(event, context):

    print(event)

    try:
        valid_signature(event)
    except Exception as e:
        logger.error(e)
        return discord_body(200, 2, 'Error Validating Discord Signature')

    body = json.loads(event['body'])

    if body['type'] == 1:
        return DISCORD_PING_PONG

    try:
        send_event_bridge_event(body)
        return discord_body(200, 5, '')
    except Exception as e:
        logger.error(e)
        return discord_body(200, 4, 'Something went wrong')
