from aws_lambda_powertools.utilities import parameters
from aws_lambda_powertools import Logger
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
import os
import json

logger = Logger(service='discord-funcs')
STAGE = os.environ.get('STAGE', 'dev')
DISCORD_PUBLIC_KEY = parameters.get_parameter(
    f'/{STAGE}/discord/starfinder/public/key', decrypt=True)

# INTERACTION RESPONSE TYPES
# NAME	VALUE	DESCRIPTION
# Pong	1	ACK a Ping
# Acknowledge	2	ACK a command without sending a message, eating the user's input
# ChannelMessage	3	respond with a message, eating the user's input
# ChannelMessageWithSource	4	respond with a message, showing the user's input
# AcknowledgeWithSource	5	ACK a command without sending a message, showing the user's input


def discord_body(status_code, type, message):
    return {
        "statusCode": status_code,
        'body': json.dumps({"type": type,
                            "data": {
                                "tts": False,
                                "content": message}})
    }


def valid_signature(event):
    body = event['body']
    auth_sig = event['headers']['x-signature-ed25519']
    auth_ts = event['headers']['x-signature-timestamp']

    message = auth_ts.encode() + body.encode()

    try:
        verify_key = VerifyKey(bytes.fromhex(DISCORD_PUBLIC_KEY))
        verify_key.verify(message, bytes.fromhex(auth_sig))
    except BadSignatureError as e:
        raise Exception(f'Signature Exception: {e}')
